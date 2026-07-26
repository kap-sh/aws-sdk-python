"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsServiceServiceRegistriesDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string


class AwsEcsServiceServiceRegistriesDetails(TypedDict, closed=True):
    container_name: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The container name value to use for the service discovery service.</p> <p>If the task definition uses the <code>bridge</code> or <code>host</code> network mode, you must specify <code>ContainerName</code> and <code>ContainerPort</code>.</p> <p>If the task definition uses the <code>awsvpc</code> network mode and a type SRV DNS record, you must specify either <code>ContainerName</code> and <code>ContainerPort</code>, or <code>Port</code> , but not both.</p>"""
    container_port: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The port value to use for the service discovery service.</p> <p>If the task definition uses the <code>bridge</code> or <code>host</code> network mode, you must specify <code>ContainerName</code> and <code>ContainerPort</code>.</p> <p>If the task definition uses the <code>awsvpc</code> network mode and a type SRV DNS record, you must specify either <code>ContainerName</code> and <code>ContainerPort</code>, or <code>Port</code> , but not both.</p>"""
    port: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The port value to use for a service discovery service that specifies an SRV record. This field can be used if both the <code>awsvpc</code>awsvpc network mode and SRV records are used.</p>"""
    registry_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the service registry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsServiceServiceRegistriesDetails) -> dict:
    out: dict = {}
    if "container_name" in value:
        out["ContainerName"] = value["container_name"]
    if "container_port" in value:
        out["ContainerPort"] = value["container_port"]
    if "port" in value:
        out["Port"] = value["port"]
    if "registry_arn" in value:
        out["RegistryArn"] = value["registry_arn"]
    return out


def deserialize_json(data: dict) -> AwsEcsServiceServiceRegistriesDetails:
    out: AwsEcsServiceServiceRegistriesDetails = {}  # type: ignore[typeddict-item]
    if "ContainerName" in data:
        out["container_name"] = data["ContainerName"]
    if "ContainerPort" in data:
        out["container_port"] = data["ContainerPort"]
    if "Port" in data:
        out["port"] = data["Port"]
    if "RegistryArn" in data:
        out["registry_arn"] = data["RegistryArn"]
    return out
