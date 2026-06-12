"""Generated from Smithy shape ``com.amazonaws.codedeploy#GreenFleetProvisioningOption``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.green_fleet_provisioning_action


class GreenFleetProvisioningOption(TypedDict):
    action: NotRequired[
        "aws_sdk_codedeploy.types.green_fleet_provisioning_action.GreenFleetProvisioningAction"
    ]
    """<p>The method used to add instances to a replacement environment.</p> <ul> <li> <p> <code>DISCOVER_EXISTING</code>: Use instances that already exist or will be created manually.</p> </li> <li> <p> <code>COPY_AUTO_SCALING_GROUP</code>: Use settings from a specified Auto Scaling group to define and create instances in a new Auto Scaling group.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GreenFleetProvisioningOption) -> dict:
    out: dict = {}
    if "action" in value:
        import aws_sdk_codedeploy.types.green_fleet_provisioning_action

        out["action"] = (
            aws_sdk_codedeploy.types.green_fleet_provisioning_action.serialize_aws_json_1_1(
                value["action"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GreenFleetProvisioningOption:
    out: GreenFleetProvisioningOption = {}  # type: ignore[typeddict-item]
    if "action" in data:
        import aws_sdk_codedeploy.types.green_fleet_provisioning_action

        out["action"] = (
            aws_sdk_codedeploy.types.green_fleet_provisioning_action.deserialize_aws_json_1_1(
                data["action"]
            )
        )
    return out
