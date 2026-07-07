"""Generated from Smithy shape ``com.amazonaws.glue#GetColumnStatisticsTaskSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.name_string


class GetColumnStatisticsTaskSettingsRequest(TypedDict, closed=True):
    database_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the database where the table resides.</p>"""
    table_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the table for which to retrieve column statistics.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetColumnStatisticsTaskSettingsRequest) -> dict:
    out: dict = {}
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetColumnStatisticsTaskSettingsRequest:
    out: GetColumnStatisticsTaskSettingsRequest = {}  # type: ignore[typeddict-item]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError(
            "GetColumnStatisticsTaskSettingsRequest.database_name required"
        )
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError(
            "GetColumnStatisticsTaskSettingsRequest.table_name required"
        )
    return out
