"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateGlobalTableOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.global_table_description


class UpdateGlobalTableOutput(TypedDict):
    global_table_description: NotRequired[
        "aws_sdk_dynamodb.types.global_table_description.GlobalTableDescription"
    ]
    """<p>Contains the details of the global table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateGlobalTableOutput) -> dict:
    out: dict = {}
    if "global_table_description" in value:
        import aws_sdk_dynamodb.types.global_table_description

        out["GlobalTableDescription"] = (
            aws_sdk_dynamodb.types.global_table_description.serialize_aws_json_1_0(
                value["global_table_description"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateGlobalTableOutput:
    out: UpdateGlobalTableOutput = {}  # type: ignore[typeddict-item]
    if "GlobalTableDescription" in data:
        import aws_sdk_dynamodb.types.global_table_description

        out["global_table_description"] = (
            aws_sdk_dynamodb.types.global_table_description.deserialize_aws_json_1_0(
                data["GlobalTableDescription"]
            )
        )
    return out
