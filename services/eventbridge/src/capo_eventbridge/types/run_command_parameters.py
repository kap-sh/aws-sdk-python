"""Generated from Smithy shape ``com.amazonaws.eventbridge#RunCommandParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eventbridge.types.run_command_targets


class RunCommandParameters(TypedDict, closed=True):
    run_command_targets: "capo_eventbridge.types.run_command_targets.RunCommandTargets"
    """<p>Currently, we support including only one RunCommandTarget block, which specifies either an array of InstanceIds or a tag.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RunCommandParameters) -> dict:
    out: dict = {}
    import capo_eventbridge.types.run_command_targets

    out["RunCommandTargets"] = (
        capo_eventbridge.types.run_command_targets.serialize_aws_json_1_1(
            value["run_command_targets"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RunCommandParameters:
    out: RunCommandParameters = {}  # type: ignore[typeddict-item]
    if "RunCommandTargets" in data:
        import capo_eventbridge.types.run_command_targets

        out["run_command_targets"] = (
            capo_eventbridge.types.run_command_targets.deserialize_aws_json_1_1(
                data["RunCommandTargets"]
            )
        )
    else:
        raise DeserializationError("RunCommandParameters.run_command_targets required")
    return out
