"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeGlobalTableInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.table_name


class DescribeGlobalTableInput(TypedDict):
    global_table_name: "aws_sdk_dynamodb.types.table_name.TableName"
    """<p>The name of the global table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeGlobalTableInput) -> dict:
    out: dict = {}
    out["GlobalTableName"] = value["global_table_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeGlobalTableInput:
    out: DescribeGlobalTableInput = {}  # type: ignore[typeddict-item]
    if "GlobalTableName" in data:
        out["global_table_name"] = data["GlobalTableName"]
    else:
        raise DeserializationError(
            "DescribeGlobalTableInput.global_table_name required"
        )
    return out
