"""Generated from Smithy shape ``com.amazonaws.ssm#SendCommandResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.command


class SendCommandResult(TypedDict, closed=True):
    command: NotRequired["capo_ssm.types.command.Command"]
    """<p>The request as it was received by Systems Manager. Also provides the command ID which can be used future references to this request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SendCommandResult) -> dict:
    out: dict = {}
    if "command" in value:
        import capo_ssm.types.command

        out["Command"] = capo_ssm.types.command.serialize_aws_json_1_1(value["command"])
    return out


def deserialize_aws_json_1_1(data: dict) -> SendCommandResult:
    out: SendCommandResult = {}  # type: ignore[typeddict-item]
    if data.get("Command") is not None:
        import capo_ssm.types.command

        out["command"] = capo_ssm.types.command.deserialize_aws_json_1_1(
            data["Command"]
        )
    return out
