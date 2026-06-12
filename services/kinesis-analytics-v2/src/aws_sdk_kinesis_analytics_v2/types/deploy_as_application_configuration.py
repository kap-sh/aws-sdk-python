"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#DeployAsApplicationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.s3_content_base_location


class DeployAsApplicationConfiguration(TypedDict):
    s3_content_location: "aws_sdk_kinesis_analytics_v2.types.s3_content_base_location.S3ContentBaseLocation"
    """<p>The description of an Amazon S3 object that contains the Amazon Data Analytics application, including the Amazon Resource Name (ARN) of the S3 bucket, the name of the Amazon S3 object that contains the data, and the version number of the Amazon S3 object that contains the data. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeployAsApplicationConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_kinesis_analytics_v2.types.s3_content_base_location

    out["S3ContentLocation"] = (
        aws_sdk_kinesis_analytics_v2.types.s3_content_base_location.serialize_aws_json_1_1(
            value["s3_content_location"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeployAsApplicationConfiguration:
    out: DeployAsApplicationConfiguration = {}  # type: ignore[typeddict-item]
    if "S3ContentLocation" in data:
        import aws_sdk_kinesis_analytics_v2.types.s3_content_base_location

        out["s3_content_location"] = (
            aws_sdk_kinesis_analytics_v2.types.s3_content_base_location.deserialize_aws_json_1_1(
                data["S3ContentLocation"]
            )
        )
    else:
        raise DeserializationError(
            "DeployAsApplicationConfiguration.s3_content_location required"
        )
    return out
