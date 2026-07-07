"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#DeployAsApplicationConfigurationUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.s3_content_base_location_update


class DeployAsApplicationConfigurationUpdate(TypedDict, closed=True):
    s3_content_location_update: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.s3_content_base_location_update.S3ContentBaseLocationUpdate"
    ]
    """<p>Updates to the location that holds the data required to specify an Amazon Data Analytics application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeployAsApplicationConfigurationUpdate) -> dict:
    out: dict = {}
    if "s3_content_location_update" in value:
        import aws_sdk_kinesis_analytics_v2.types.s3_content_base_location_update

        out["S3ContentLocationUpdate"] = (
            aws_sdk_kinesis_analytics_v2.types.s3_content_base_location_update.serialize_aws_json_1_1(
                value["s3_content_location_update"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeployAsApplicationConfigurationUpdate:
    out: DeployAsApplicationConfigurationUpdate = {}  # type: ignore[typeddict-item]
    if "S3ContentLocationUpdate" in data:
        import aws_sdk_kinesis_analytics_v2.types.s3_content_base_location_update

        out["s3_content_location_update"] = (
            aws_sdk_kinesis_analytics_v2.types.s3_content_base_location_update.deserialize_aws_json_1_1(
                data["S3ContentLocationUpdate"]
            )
        )
    return out
