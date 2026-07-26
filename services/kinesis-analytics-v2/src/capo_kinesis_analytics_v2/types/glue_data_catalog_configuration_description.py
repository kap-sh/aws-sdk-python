"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#GlueDataCatalogConfigurationDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.database_arn


class GlueDataCatalogConfigurationDescription(TypedDict, closed=True):
    database_arn: "capo_kinesis_analytics_v2.types.database_arn.DatabaseARN"
    """<p>The Amazon Resource Name (ARN) of the database.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GlueDataCatalogConfigurationDescription) -> dict:
    out: dict = {}
    out["DatabaseARN"] = value["database_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GlueDataCatalogConfigurationDescription:
    out: GlueDataCatalogConfigurationDescription = {}  # type: ignore[typeddict-item]
    if "DatabaseARN" in data:
        out["database_arn"] = data["DatabaseARN"]
    else:
        raise DeserializationError(
            "GlueDataCatalogConfigurationDescription.database_arn required"
        )
    return out
