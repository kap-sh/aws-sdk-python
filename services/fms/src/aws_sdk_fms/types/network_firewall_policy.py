"""Generated from Smithy shape ``com.amazonaws.fms#NetworkFirewallPolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fms.types.firewall_deployment_model


class NetworkFirewallPolicy(TypedDict):
    firewall_deployment_model: NotRequired[
        "aws_sdk_fms.types.firewall_deployment_model.FirewallDeploymentModel"
    ]
    """<p>Defines the deployment model to use for the firewall policy. To use a distributed model, set <a href=\"https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_PolicyOption.html\">PolicyOption</a> to <code>NULL</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkFirewallPolicy) -> dict:
    out: dict = {}
    if "firewall_deployment_model" in value:
        import aws_sdk_fms.types.firewall_deployment_model

        out["FirewallDeploymentModel"] = (
            aws_sdk_fms.types.firewall_deployment_model.serialize_aws_json_1_1(
                value["firewall_deployment_model"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> NetworkFirewallPolicy:
    out: NetworkFirewallPolicy = {}  # type: ignore[typeddict-item]
    if "FirewallDeploymentModel" in data:
        import aws_sdk_fms.types.firewall_deployment_model

        out["firewall_deployment_model"] = (
            aws_sdk_fms.types.firewall_deployment_model.deserialize_aws_json_1_1(
                data["FirewallDeploymentModel"]
            )
        )
    return out
