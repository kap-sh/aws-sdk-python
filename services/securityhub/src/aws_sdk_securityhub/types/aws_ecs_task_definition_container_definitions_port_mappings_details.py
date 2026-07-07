"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetails(
    TypedDict, closed=True
):
    container_port: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The port number on the container that is bound to the user-specified or automatically assigned host port.</p>"""
    host_port: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The port number on the container instance to reserve for the container.</p>"""
    protocol: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The protocol used for the port mapping. The default is <code>tcp</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetails,
) -> dict:
    out: dict = {}
    if "container_port" in value:
        out["ContainerPort"] = value["container_port"]
    if "host_port" in value:
        out["HostPort"] = value["host_port"]
    if "protocol" in value:
        out["Protocol"] = value["protocol"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetails:
    out: AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetails = {}  # type: ignore[typeddict-item]
    if "ContainerPort" in data:
        out["container_port"] = data["ContainerPort"]
    if "HostPort" in data:
        out["host_port"] = data["HostPort"]
    if "Protocol" in data:
        out["protocol"] = data["Protocol"]
    return out
