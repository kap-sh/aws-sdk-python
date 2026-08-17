"""Generated from Smithy shape ``com.amazonaws.dynamodb#CreateTableOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.table_description


class CreateTableOutput(TypedDict, closed=True):
    table_description: NotRequired[
        "capo_dynamodb.types.table_description.TableDescription"
    ]
    """<p>Represents the properties of the table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateTableOutput) -> dict:
    out: dict = {}
    if "table_description" in value:
        import capo_dynamodb.types.table_description

        out["TableDescription"] = (
            capo_dynamodb.types.table_description.serialize_aws_json_1_0(
                value["table_description"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateTableOutput:
    out: CreateTableOutput = {}  # type: ignore[typeddict-item]
    if data.get("TableDescription") is not None:
        import capo_dynamodb.types.table_description

        out["table_description"] = (
            capo_dynamodb.types.table_description.deserialize_aws_json_1_0(
                data["TableDescription"]
            )
        )
    return out
