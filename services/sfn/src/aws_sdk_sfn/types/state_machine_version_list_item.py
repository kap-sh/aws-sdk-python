"""Generated from Smithy shape ``com.amazonaws.sfn#StateMachineVersionListItem``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.long_arn
    import aws_sdk_sfn.types.timestamp


class StateMachineVersionListItem(TypedDict):
    state_machine_version_arn: "aws_sdk_sfn.types.long_arn.LongArn"
    """<p>The Amazon Resource Name (ARN) that identifies a state machine version. The version ARN is a combination of state machine ARN and the version number separated by a colon (:). For example, <code>stateMachineARN:1</code>.</p>"""
    creation_date: "aws_sdk_sfn.types.timestamp.Timestamp"
    """<p>The creation date of a state machine version.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StateMachineVersionListItem) -> dict:
    out: dict = {}
    out["stateMachineVersionArn"] = value["state_machine_version_arn"]
    import aws_sdk_sfn.types.timestamp

    out["creationDate"] = aws_sdk_sfn.types.timestamp.serialize_aws_json_1_0(
        value["creation_date"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> StateMachineVersionListItem:
    out: StateMachineVersionListItem = {}  # type: ignore[typeddict-item]
    if "stateMachineVersionArn" in data:
        out["state_machine_version_arn"] = data["stateMachineVersionArn"]
    else:
        raise DeserializationError(
            "StateMachineVersionListItem.state_machine_version_arn required"
        )
    if "creationDate" in data:
        import aws_sdk_sfn.types.timestamp

        out["creation_date"] = aws_sdk_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["creationDate"]
        )
    else:
        raise DeserializationError("StateMachineVersionListItem.creation_date required")
    return out
