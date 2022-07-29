import boto3
import progressbar
from botocore.exceptions import NoCredentialsError


def download_from_s3(bucket, s3_file, local_file):
    s3 = boto3.resource('s3')
    # s3 = boto3.client('s3')
    # response = s3.head_object(Bucket=bucket, Key=s3_file)
    size = 12321971913
    up_progress = progressbar.progressbar.ProgressBar(maxval=size)
    up_progress.start()

    def upload_progress(chunk):
        up_progress.update(up_progress.currval + chunk)

    try:
        s3.download_file(bucket, s3_file, local_file, Callback=upload_progress)
        up_progress.finish()
        print("Download Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False