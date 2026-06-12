"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeRuntimeConfigurationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.runtime_configuration


class DescribeRuntimeConfigurationOutput(TypedDict):
    runtime_configuration: NotRequired[
        "aws_sdk_gamelift.types.runtime_configuration.RuntimeConfiguration"
    ]
    """<p>Instructions that describe how server processes are launched and maintained on computes in the fleet.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRuntimeConfigurationOutput) -> dict:
    out: dict = {}
    if "runtime_configuration" in value:
        import aws_sdk_gamelift.types.runtime_configuration

        out["RuntimeConfiguration"] = (
            aws_sdk_gamelift.types.runtime_configuration.serialize_aws_json_1_1(
                value["runtime_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRuntimeConfigurationOutput:
    out: DescribeRuntimeConfigurationOutput = {}  # type: ignore[typeddict-item]
    if "RuntimeConfiguration" in data:
        import aws_sdk_gamelift.types.runtime_configuration

        out["runtime_configuration"] = (
            aws_sdk_gamelift.types.runtime_configuration.deserialize_aws_json_1_1(
                data["RuntimeConfiguration"]
            )
        )
    return out
