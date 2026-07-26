"""Generated from Smithy shape ``com.amazonaws.gamelift#UpdateRuntimeConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.runtime_configuration


class UpdateRuntimeConfigurationOutput(TypedDict, closed=True):
    runtime_configuration: NotRequired[
        "capo_gamelift.types.runtime_configuration.RuntimeConfiguration"
    ]
    """<p>The runtime configuration currently in use by computes in the fleet. If the update is successful, all property changes are shown. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateRuntimeConfigurationOutput) -> dict:
    out: dict = {}
    if "runtime_configuration" in value:
        import capo_gamelift.types.runtime_configuration

        out["RuntimeConfiguration"] = (
            capo_gamelift.types.runtime_configuration.serialize_aws_json_1_1(
                value["runtime_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateRuntimeConfigurationOutput:
    out: UpdateRuntimeConfigurationOutput = {}  # type: ignore[typeddict-item]
    if "RuntimeConfiguration" in data:
        import capo_gamelift.types.runtime_configuration

        out["runtime_configuration"] = (
            capo_gamelift.types.runtime_configuration.deserialize_aws_json_1_1(
                data["RuntimeConfiguration"]
            )
        )
    return out
