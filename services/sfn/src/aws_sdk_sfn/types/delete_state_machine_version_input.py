"""Generated from Smithy shape ``com.amazonaws.sfn#DeleteStateMachineVersionInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.long_arn


class DeleteStateMachineVersionInput(TypedDict):
    state_machine_version_arn: "aws_sdk_sfn.types.long_arn.LongArn"
    """<p>The Amazon Resource Name (ARN) of the state machine version to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteStateMachineVersionInput) -> dict:
    out: dict = {}
    out["stateMachineVersionArn"] = value["state_machine_version_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteStateMachineVersionInput:
    out: DeleteStateMachineVersionInput = {}  # type: ignore[typeddict-item]
    if "stateMachineVersionArn" in data:
        out["state_machine_version_arn"] = data["stateMachineVersionArn"]
    else:
        raise DeserializationError(
            "DeleteStateMachineVersionInput.state_machine_version_arn required"
        )
    return out
