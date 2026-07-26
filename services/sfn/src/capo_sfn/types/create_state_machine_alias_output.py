"""Generated from Smithy shape ``com.amazonaws.sfn#CreateStateMachineAliasOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sfn.types.arn
    import capo_sfn.types.timestamp


class CreateStateMachineAliasOutput(TypedDict, closed=True):
    state_machine_alias_arn: "capo_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that identifies the created state machine alias.</p>"""
    creation_date: "capo_sfn.types.timestamp.Timestamp"
    """<p>The date the state machine alias was created.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateStateMachineAliasOutput) -> dict:
    out: dict = {}
    out["stateMachineAliasArn"] = value["state_machine_alias_arn"]
    import capo_sfn.types.timestamp

    out["creationDate"] = capo_sfn.types.timestamp.serialize_aws_json_1_0(
        value["creation_date"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateStateMachineAliasOutput:
    out: CreateStateMachineAliasOutput = {}  # type: ignore[typeddict-item]
    if "stateMachineAliasArn" in data:
        out["state_machine_alias_arn"] = data["stateMachineAliasArn"]
    else:
        raise DeserializationError(
            "CreateStateMachineAliasOutput.state_machine_alias_arn required"
        )
    if "creationDate" in data:
        import capo_sfn.types.timestamp

        out["creation_date"] = capo_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["creationDate"]
        )
    else:
        raise DeserializationError(
            "CreateStateMachineAliasOutput.creation_date required"
        )
    return out
