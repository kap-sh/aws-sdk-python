"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerServiceStateDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.container_service_state_detail_code
    import capo_lightsail.types.string


class ContainerServiceStateDetail(TypedDict, closed=True):
    code: NotRequired[
        "capo_lightsail.types.container_service_state_detail_code.ContainerServiceStateDetailCode"
    ]
    """<p>The state code of the container service.</p> <p>The following state codes are possible:</p> <ul> <li> <p>The following state codes are possible if your container service is in a <code>DEPLOYING</code> or <code>UPDATING</code> state:</p> <ul> <li> <p> <code>CREATING_SYSTEM_RESOURCES</code> - The system resources for your container service are being created.</p> </li> <li> <p> <code>CREATING_NETWORK_INFRASTRUCTURE</code> - The network infrastructure for your container service are being created.</p> </li> <li> <p> <code>PROVISIONING_CERTIFICATE</code> - The SSL/TLS certificate for your container service is being created.</p> </li> <li> <p> <code>PROVISIONING_SERVICE</code> - Your container service is being provisioned.</p> </li> <li> <p> <code>CREATING_DEPLOYMENT</code> - Your deployment is being created on your container service.</p> </li> <li> <p> <code>EVALUATING_HEALTH_CHECK</code> - The health of your deployment is being evaluated.</p> </li> <li> <p> <code>ACTIVATING_DEPLOYMENT</code> - Your deployment is being activated.</p> </li> </ul> </li> <li> <p>The following state codes are possible if your container service is in a <code>PENDING</code> state:</p> <ul> <li> <p> <code>CERTIFICATE_LIMIT_EXCEEDED</code> - The SSL/TLS certificate required for your container service exceeds the maximum number of certificates allowed for your account.</p> </li> <li> <p> <code>UNKNOWN_ERROR</code> - An error was experienced when your container service was being created.</p> </li> </ul> </li> </ul>"""
    message: NotRequired["capo_lightsail.types.string.string"]
    """<p>A message that provides more information for the state code.</p> <note> <p>The state detail is populated only when a container service is in a <code>PENDING</code>, <code>DEPLOYING</code>, or <code>UPDATING</code> state.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerServiceStateDetail) -> dict:
    out: dict = {}
    if "code" in value:
        import capo_lightsail.types.container_service_state_detail_code

        out["code"] = (
            capo_lightsail.types.container_service_state_detail_code.serialize_aws_json_1_1(
                value["code"]
            )
        )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerServiceStateDetail:
    out: ContainerServiceStateDetail = {}  # type: ignore[typeddict-item]
    if "code" in data:
        import capo_lightsail.types.container_service_state_detail_code

        out["code"] = (
            capo_lightsail.types.container_service_state_detail_code.deserialize_aws_json_1_1(
                data["code"]
            )
        )
    if "message" in data:
        out["message"] = data["message"]
    return out
