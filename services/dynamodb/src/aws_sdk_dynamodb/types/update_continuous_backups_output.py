"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateContinuousBackupsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.continuous_backups_description


class UpdateContinuousBackupsOutput(TypedDict):
    continuous_backups_description: NotRequired[
        "aws_sdk_dynamodb.types.continuous_backups_description.ContinuousBackupsDescription"
    ]
    """<p>Represents the continuous backups and point in time recovery settings on the table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateContinuousBackupsOutput) -> dict:
    out: dict = {}
    if "continuous_backups_description" in value:
        import aws_sdk_dynamodb.types.continuous_backups_description

        out["ContinuousBackupsDescription"] = (
            aws_sdk_dynamodb.types.continuous_backups_description.serialize_aws_json_1_0(
                value["continuous_backups_description"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateContinuousBackupsOutput:
    out: UpdateContinuousBackupsOutput = {}  # type: ignore[typeddict-item]
    if "ContinuousBackupsDescription" in data:
        import aws_sdk_dynamodb.types.continuous_backups_description

        out["continuous_backups_description"] = (
            aws_sdk_dynamodb.types.continuous_backups_description.deserialize_aws_json_1_0(
                data["ContinuousBackupsDescription"]
            )
        )
    return out
