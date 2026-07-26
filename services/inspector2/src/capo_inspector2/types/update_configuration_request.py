"""Generated from Smithy shape ``com.amazonaws.inspector2#UpdateConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.ec2_configuration
    import capo_inspector2.types.ecr_configuration


class UpdateConfigurationRequest(TypedDict, closed=True):
    ecr_configuration: NotRequired[
        "capo_inspector2.types.ecr_configuration.EcrConfiguration"
    ]
    """<p>Specifies how the ECR automated re-scan will be updated for your environment.</p>"""
    ec2_configuration: NotRequired[
        "capo_inspector2.types.ec2_configuration.Ec2Configuration"
    ]
    """<p>Specifies how the Amazon EC2 automated scan will be updated for your environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConfigurationRequest) -> dict:
    out: dict = {}
    if "ecr_configuration" in value:
        import capo_inspector2.types.ecr_configuration

        out["ecrConfiguration"] = (
            capo_inspector2.types.ecr_configuration.serialize_json(
                value["ecr_configuration"]
            )
        )
    if "ec2_configuration" in value:
        import capo_inspector2.types.ec2_configuration

        out["ec2Configuration"] = (
            capo_inspector2.types.ec2_configuration.serialize_json(
                value["ec2_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateConfigurationRequest:
    out: UpdateConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "ecrConfiguration" in data:
        import capo_inspector2.types.ecr_configuration

        out["ecr_configuration"] = (
            capo_inspector2.types.ecr_configuration.deserialize_json(
                data["ecrConfiguration"]
            )
        )
    if "ec2Configuration" in data:
        import capo_inspector2.types.ec2_configuration

        out["ec2_configuration"] = (
            capo_inspector2.types.ec2_configuration.deserialize_json(
                data["ec2Configuration"]
            )
        )
    return out
