"""Generated from Smithy shape ``com.amazonaws.inspector2#GetConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.ec2_configuration_state
    import aws_sdk_inspector2.types.ecr_configuration_state


class GetConfigurationResponse(TypedDict):
    ecr_configuration: NotRequired[
        "aws_sdk_inspector2.types.ecr_configuration_state.EcrConfigurationState"
    ]
    """<p>Specifies how the ECR automated re-scan duration is currently configured for your environment.</p>"""
    ec2_configuration: NotRequired[
        "aws_sdk_inspector2.types.ec2_configuration_state.Ec2ConfigurationState"
    ]
    """<p>Specifies how the Amazon EC2 automated scan mode is currently configured for your environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfigurationResponse) -> dict:
    out: dict = {}
    if "ecr_configuration" in value:
        import aws_sdk_inspector2.types.ecr_configuration_state

        out["ecrConfiguration"] = (
            aws_sdk_inspector2.types.ecr_configuration_state.serialize_json(
                value["ecr_configuration"]
            )
        )
    if "ec2_configuration" in value:
        import aws_sdk_inspector2.types.ec2_configuration_state

        out["ec2Configuration"] = (
            aws_sdk_inspector2.types.ec2_configuration_state.serialize_json(
                value["ec2_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetConfigurationResponse:
    out: GetConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "ecrConfiguration" in data:
        import aws_sdk_inspector2.types.ecr_configuration_state

        out["ecr_configuration"] = (
            aws_sdk_inspector2.types.ecr_configuration_state.deserialize_json(
                data["ecrConfiguration"]
            )
        )
    if "ec2Configuration" in data:
        import aws_sdk_inspector2.types.ec2_configuration_state

        out["ec2_configuration"] = (
            aws_sdk_inspector2.types.ec2_configuration_state.deserialize_json(
                data["ec2Configuration"]
            )
        )
    return out
