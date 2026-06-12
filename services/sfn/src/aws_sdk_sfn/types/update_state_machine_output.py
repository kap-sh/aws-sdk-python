"""Generated from Smithy shape ``com.amazonaws.sfn#UpdateStateMachineOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.arn
    import aws_sdk_sfn.types.revision_id
    import aws_sdk_sfn.types.timestamp


class UpdateStateMachineOutput(TypedDict):
    update_date: "aws_sdk_sfn.types.timestamp.Timestamp"
    """<p>The date and time the state machine was updated.</p>"""
    revision_id: NotRequired["aws_sdk_sfn.types.revision_id.RevisionId"]
    """<p>The revision identifier for the updated state machine.</p>"""
    state_machine_version_arn: NotRequired["aws_sdk_sfn.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the published state machine version.</p> <p>If the <code>publish</code> parameter isn't set to <code>true</code>, this field returns null.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateStateMachineOutput) -> dict:
    out: dict = {}
    import aws_sdk_sfn.types.timestamp

    out["updateDate"] = aws_sdk_sfn.types.timestamp.serialize_aws_json_1_0(
        value["update_date"]
    )
    if "revision_id" in value:
        out["revisionId"] = value["revision_id"]
    if "state_machine_version_arn" in value:
        out["stateMachineVersionArn"] = value["state_machine_version_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateStateMachineOutput:
    out: UpdateStateMachineOutput = {}  # type: ignore[typeddict-item]
    if "updateDate" in data:
        import aws_sdk_sfn.types.timestamp

        out["update_date"] = aws_sdk_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["updateDate"]
        )
    else:
        raise DeserializationError("UpdateStateMachineOutput.update_date required")
    if "revisionId" in data:
        out["revision_id"] = data["revisionId"]
    if "stateMachineVersionArn" in data:
        out["state_machine_version_arn"] = data["stateMachineVersionArn"]
    return out
