"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerGroupPortMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.container_port_mapping_list
    import capo_gamelift.types.non_empty_string
    import capo_gamelift.types.non_zero_and128_max_ascii_string


class ContainerGroupPortMapping(TypedDict, closed=True):
    container_name: NotRequired[
        "capo_gamelift.types.non_zero_and128_max_ascii_string.NonZeroAnd128MaxAsciiString"
    ]
    """<p>The name of the container, as defined in the container group definition.</p>"""
    container_runtime_id: NotRequired[
        "capo_gamelift.types.non_empty_string.NonEmptyString"
    ]
    """<p>The runtime ID for the container that's running in a compute. This value is unique within the compute.</p>"""
    container_port_mappings: NotRequired[
        "capo_gamelift.types.container_port_mapping_list.ContainerPortMappingList"
    ]
    """<p>A list of <code>ContainerPortMapping</code> objects that describe the port mappings for this container.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerGroupPortMapping) -> dict:
    out: dict = {}
    if "container_name" in value:
        out["ContainerName"] = value["container_name"]
    if "container_runtime_id" in value:
        out["ContainerRuntimeId"] = value["container_runtime_id"]
    if "container_port_mappings" in value:
        import capo_gamelift.types.container_port_mapping_list

        out["ContainerPortMappings"] = (
            capo_gamelift.types.container_port_mapping_list.serialize_aws_json_1_1(
                value["container_port_mappings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerGroupPortMapping:
    out: ContainerGroupPortMapping = {}  # type: ignore[typeddict-item]
    if "ContainerName" in data:
        out["container_name"] = data["ContainerName"]
    if "ContainerRuntimeId" in data:
        out["container_runtime_id"] = data["ContainerRuntimeId"]
    if "ContainerPortMappings" in data:
        import capo_gamelift.types.container_port_mapping_list

        out["container_port_mappings"] = (
            capo_gamelift.types.container_port_mapping_list.deserialize_aws_json_1_1(
                data["ContainerPortMappings"]
            )
        )
    return out
