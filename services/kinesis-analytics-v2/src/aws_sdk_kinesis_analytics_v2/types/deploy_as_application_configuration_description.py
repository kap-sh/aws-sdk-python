"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#DeployAsApplicationConfigurationDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.s3_content_base_location_description


class DeployAsApplicationConfigurationDescription(TypedDict, closed=True):
    s3_content_location_description: "aws_sdk_kinesis_analytics_v2.types.s3_content_base_location_description.S3ContentBaseLocationDescription"
    """<p>The location that holds the data required to specify an Amazon Data Analytics application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeployAsApplicationConfigurationDescription) -> dict:
    out: dict = {}
    import aws_sdk_kinesis_analytics_v2.types.s3_content_base_location_description

    out["S3ContentLocationDescription"] = (
        aws_sdk_kinesis_analytics_v2.types.s3_content_base_location_description.serialize_aws_json_1_1(
            value["s3_content_location_description"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeployAsApplicationConfigurationDescription:
    out: DeployAsApplicationConfigurationDescription = {}  # type: ignore[typeddict-item]
    if "S3ContentLocationDescription" in data:
        import aws_sdk_kinesis_analytics_v2.types.s3_content_base_location_description

        out["s3_content_location_description"] = (
            aws_sdk_kinesis_analytics_v2.types.s3_content_base_location_description.deserialize_aws_json_1_1(
                data["S3ContentLocationDescription"]
            )
        )
    else:
        raise DeserializationError(
            "DeployAsApplicationConfigurationDescription.s3_content_location_description required"
        )
    return out
