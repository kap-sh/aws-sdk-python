"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeGlobalTableSettingsInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.table_name


class DescribeGlobalTableSettingsInput(TypedDict):
    global_table_name: "aws_sdk_dynamodb.types.table_name.TableName"
    """<p>The name of the global table to describe.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeGlobalTableSettingsInput) -> dict:
    out: dict = {}
    out["GlobalTableName"] = value["global_table_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeGlobalTableSettingsInput:
    out: DescribeGlobalTableSettingsInput = {}  # type: ignore[typeddict-item]
    if "GlobalTableName" in data:
        out["global_table_name"] = data["GlobalTableName"]
    else:
        raise DeserializationError(
            "DescribeGlobalTableSettingsInput.global_table_name required"
        )
    return out
