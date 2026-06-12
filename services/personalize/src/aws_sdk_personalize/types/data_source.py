"""Generated from Smithy shape ``com.amazonaws.personalize#DataSource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_personalize.types.s3_location


class DataSource(TypedDict):
    data_location: NotRequired["aws_sdk_personalize.types.s3_location.S3Location"]
    """<p>For dataset import jobs, the path to the Amazon S3 bucket where the data that you want to upload to your dataset is stored. For data deletion jobs, the path to the Amazon S3 bucket that stores the list of records to delete. </p> <p> For example: </p> <p> <code>s3://bucket-name/folder-name/fileName.csv</code> </p> <p>If your CSV files are in a folder in your Amazon S3 bucket and you want your import job or data deletion job to consider multiple files, you can specify the path to the folder. With a data deletion job, Amazon Personalize uses all files in the folder and any sub folder. Use the following syntax with a <code>/</code> after the folder name:</p> <p> <code>s3://bucket-name/folder-name/</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataSource) -> dict:
    out: dict = {}
    if "data_location" in value:
        out["dataLocation"] = value["data_location"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataSource:
    out: DataSource = {}  # type: ignore[typeddict-item]
    if "dataLocation" in data:
        out["data_location"] = data["dataLocation"]
    return out
