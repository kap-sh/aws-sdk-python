"""Generated from Smithy shape ``com.amazonaws.gamelift#UpdateRuntimeConfigurationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.runtime_configuration


class UpdateRuntimeConfigurationOutput(TypedDict):
    runtime_configuration: NotRequired[
        "aws_sdk_gamelift.types.runtime_configuration.RuntimeConfiguration"
    ]
    """<p>The runtime configuration currently in use by computes in the fleet. If the update is successful, all property changes are shown. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateRuntimeConfigurationOutput) -> dict:
    out: dict = {}
    if "runtime_configuration" in value:
        import aws_sdk_gamelift.types.runtime_configuration

        out["RuntimeConfiguration"] = (
            aws_sdk_gamelift.types.runtime_configuration.serialize_aws_json_1_1(
                value["runtime_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateRuntimeConfigurationOutput:
    out: UpdateRuntimeConfigurationOutput = {}  # type: ignore[typeddict-item]
    if "RuntimeConfiguration" in data:
        import aws_sdk_gamelift.types.runtime_configuration

        out["runtime_configuration"] = (
            aws_sdk_gamelift.types.runtime_configuration.deserialize_aws_json_1_1(
                data["RuntimeConfiguration"]
            )
        )
    return out
