"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeGlobalTableOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.global_table_description


class DescribeGlobalTableOutput(TypedDict, closed=True):
    global_table_description: NotRequired[
        "aws_sdk_dynamodb.types.global_table_description.GlobalTableDescription"
    ]
    """<p>Contains the details of the global table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeGlobalTableOutput) -> dict:
    out: dict = {}
    if "global_table_description" in value:
        import aws_sdk_dynamodb.types.global_table_description

        out["GlobalTableDescription"] = (
            aws_sdk_dynamodb.types.global_table_description.serialize_aws_json_1_0(
                value["global_table_description"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeGlobalTableOutput:
    out: DescribeGlobalTableOutput = {}  # type: ignore[typeddict-item]
    if "GlobalTableDescription" in data:
        import aws_sdk_dynamodb.types.global_table_description

        out["global_table_description"] = (
            aws_sdk_dynamodb.types.global_table_description.deserialize_aws_json_1_0(
                data["GlobalTableDescription"]
            )
        )
    return out
