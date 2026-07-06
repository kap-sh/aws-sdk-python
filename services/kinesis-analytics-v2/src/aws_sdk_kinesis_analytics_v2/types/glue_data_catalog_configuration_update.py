"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#GlueDataCatalogConfigurationUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.database_arn


class GlueDataCatalogConfigurationUpdate(TypedDict, closed=True):
    database_arn_update: "aws_sdk_kinesis_analytics_v2.types.database_arn.DatabaseARN"
    """<p>The updated Amazon Resource Name (ARN) of the database.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GlueDataCatalogConfigurationUpdate) -> dict:
    out: dict = {}
    out["DatabaseARNUpdate"] = value["database_arn_update"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GlueDataCatalogConfigurationUpdate:
    out: GlueDataCatalogConfigurationUpdate = {}  # type: ignore[typeddict-item]
    if "DatabaseARNUpdate" in data:
        out["database_arn_update"] = data["DatabaseARNUpdate"]
    else:
        raise DeserializationError(
            "GlueDataCatalogConfigurationUpdate.database_arn_update required"
        )
    return out
