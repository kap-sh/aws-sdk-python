"""Generated from Smithy shape ``com.amazonaws.sfn#UpdateStateMachineAliasOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.timestamp


class UpdateStateMachineAliasOutput(TypedDict, closed=True):
    update_date: "aws_sdk_sfn.types.timestamp.Timestamp"
    """<p>The date and time the state machine alias was updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateStateMachineAliasOutput) -> dict:
    out: dict = {}
    import aws_sdk_sfn.types.timestamp

    out["updateDate"] = aws_sdk_sfn.types.timestamp.serialize_aws_json_1_0(
        value["update_date"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateStateMachineAliasOutput:
    out: UpdateStateMachineAliasOutput = {}  # type: ignore[typeddict-item]
    if "updateDate" in data:
        import aws_sdk_sfn.types.timestamp

        out["update_date"] = aws_sdk_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["updateDate"]
        )
    else:
        raise DeserializationError("UpdateStateMachineAliasOutput.update_date required")
    return out
