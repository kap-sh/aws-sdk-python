"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.action_configuration_map


class ActionConfiguration(TypedDict, closed=True):
    configuration: NotRequired[
        "aws_sdk_codepipeline.types.action_configuration_map.ActionConfigurationMap"
    ]
    """<p>The configuration data for the action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionConfiguration) -> dict:
    out: dict = {}
    if "configuration" in value:
        import aws_sdk_codepipeline.types.action_configuration_map

        out["configuration"] = (
            aws_sdk_codepipeline.types.action_configuration_map.serialize_aws_json_1_1(
                value["configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ActionConfiguration:
    out: ActionConfiguration = {}  # type: ignore[typeddict-item]
    if "configuration" in data:
        import aws_sdk_codepipeline.types.action_configuration_map

        out["configuration"] = (
            aws_sdk_codepipeline.types.action_configuration_map.deserialize_aws_json_1_1(
                data["configuration"]
            )
        )
    return out
