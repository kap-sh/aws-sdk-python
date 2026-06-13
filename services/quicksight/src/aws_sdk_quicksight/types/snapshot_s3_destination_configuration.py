"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotS3DestinationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.s3_bucket_configuration


class SnapshotS3DestinationConfiguration(TypedDict):
    bucket_configuration: (
        "aws_sdk_quicksight.types.s3_bucket_configuration.S3BucketConfiguration"
    )
    """<p>A structure that contains details about the Amazon S3 bucket that the generated dashboard snapshot is saved in.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotS3DestinationConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.s3_bucket_configuration

    out["BucketConfiguration"] = (
        aws_sdk_quicksight.types.s3_bucket_configuration.serialize_json(
            value["bucket_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> SnapshotS3DestinationConfiguration:
    out: SnapshotS3DestinationConfiguration = {}  # type: ignore[typeddict-item]
    if "BucketConfiguration" in data:
        import aws_sdk_quicksight.types.s3_bucket_configuration

        out["bucket_configuration"] = (
            aws_sdk_quicksight.types.s3_bucket_configuration.deserialize_json(
                data["BucketConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "SnapshotS3DestinationConfiguration.bucket_configuration required"
        )
    return out
