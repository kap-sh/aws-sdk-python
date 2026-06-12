"""Generated from Smithy shape ``com.amazonaws.sfn#StateMachineAliasListItem``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.long_arn
    import aws_sdk_sfn.types.timestamp


class StateMachineAliasListItem(TypedDict):
    state_machine_alias_arn: "aws_sdk_sfn.types.long_arn.LongArn"
    """<p>The Amazon Resource Name (ARN) that identifies a state machine alias. The alias ARN is a combination of state machine ARN and the alias name separated by a colon (:). For example, <code>stateMachineARN:PROD</code>.</p>"""
    creation_date: "aws_sdk_sfn.types.timestamp.Timestamp"
    """<p>The creation date of a state machine alias.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StateMachineAliasListItem) -> dict:
    out: dict = {}
    out["stateMachineAliasArn"] = value["state_machine_alias_arn"]
    import aws_sdk_sfn.types.timestamp

    out["creationDate"] = aws_sdk_sfn.types.timestamp.serialize_aws_json_1_0(
        value["creation_date"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> StateMachineAliasListItem:
    out: StateMachineAliasListItem = {}  # type: ignore[typeddict-item]
    if "stateMachineAliasArn" in data:
        out["state_machine_alias_arn"] = data["stateMachineAliasArn"]
    else:
        raise DeserializationError(
            "StateMachineAliasListItem.state_machine_alias_arn required"
        )
    if "creationDate" in data:
        import aws_sdk_sfn.types.timestamp

        out["creation_date"] = aws_sdk_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["creationDate"]
        )
    else:
        raise DeserializationError("StateMachineAliasListItem.creation_date required")
    return out
