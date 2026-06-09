"""Generated from Smithy shape ``com.amazonaws.dynamodb#RestoreTableFromBackupOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.table_description


class RestoreTableFromBackupOutput(TypedDict):
    table_description: NotRequired[
        "aws_sdk_dynamodb.types.table_description.TableDescription"
    ]
    """<p>The description of the table created from an existing backup.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RestoreTableFromBackupOutput) -> dict:
    out: dict = {}
    if "table_description" in value:
        import aws_sdk_dynamodb.types.table_description

        out["TableDescription"] = (
            aws_sdk_dynamodb.types.table_description.serialize_aws_json_1_0(
                value["table_description"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RestoreTableFromBackupOutput:
    out: RestoreTableFromBackupOutput = {}  # type: ignore[typeddict-item]
    if "TableDescription" in data:
        import aws_sdk_dynamodb.types.table_description

        out["table_description"] = (
            aws_sdk_dynamodb.types.table_description.deserialize_aws_json_1_0(
                data["TableDescription"]
            )
        )
    return out
