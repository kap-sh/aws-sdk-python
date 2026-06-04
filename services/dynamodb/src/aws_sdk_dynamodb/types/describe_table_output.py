"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeTableOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.table_description


class DescribeTableOutput(TypedDict):
    table: NotRequired["aws_sdk_dynamodb.types.table_description.TableDescription"]
    """<p>The properties of the table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeTableOutput) -> dict:
    out: dict = {}
    if "table" in value:
        import aws_sdk_dynamodb.types.table_description

        out["Table"] = aws_sdk_dynamodb.types.table_description.serialize_aws_json_1_0(
            value["table"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeTableOutput:
    out: DescribeTableOutput = {}  # type: ignore[typeddict-item]
    if "Table" in data:
        import aws_sdk_dynamodb.types.table_description

        out["table"] = (
            aws_sdk_dynamodb.types.table_description.deserialize_aws_json_1_0(
                data["Table"]
            )
        )
    return out
