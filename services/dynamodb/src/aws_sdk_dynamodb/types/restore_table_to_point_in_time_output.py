"""Generated from Smithy shape ``com.amazonaws.dynamodb#RestoreTableToPointInTimeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.table_description


class RestoreTableToPointInTimeOutput(TypedDict, closed=True):
    table_description: NotRequired[
        "aws_sdk_dynamodb.types.table_description.TableDescription"
    ]
    """<p>Represents the properties of a table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RestoreTableToPointInTimeOutput) -> dict:
    out: dict = {}
    if "table_description" in value:
        import aws_sdk_dynamodb.types.table_description

        out["TableDescription"] = (
            aws_sdk_dynamodb.types.table_description.serialize_aws_json_1_0(
                value["table_description"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RestoreTableToPointInTimeOutput:
    out: RestoreTableToPointInTimeOutput = {}  # type: ignore[typeddict-item]
    if "TableDescription" in data:
        import aws_sdk_dynamodb.types.table_description

        out["table_description"] = (
            aws_sdk_dynamodb.types.table_description.deserialize_aws_json_1_0(
                data["TableDescription"]
            )
        )
    return out
