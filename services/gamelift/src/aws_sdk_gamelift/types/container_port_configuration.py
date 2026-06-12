"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerPortConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.container_port_range_list


class ContainerPortConfiguration(TypedDict):
    container_port_ranges: NotRequired[
        "aws_sdk_gamelift.types.container_port_range_list.ContainerPortRangeList"
    ]
    """<p>A set of one or more container port number ranges. The ranges can't overlap if the ranges' network protocols are the same. Overlapping ranges with different protocols is allowed but not recommended. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerPortConfiguration) -> dict:
    out: dict = {}
    if "container_port_ranges" in value:
        import aws_sdk_gamelift.types.container_port_range_list

        out["ContainerPortRanges"] = (
            aws_sdk_gamelift.types.container_port_range_list.serialize_aws_json_1_1(
                value["container_port_ranges"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerPortConfiguration:
    out: ContainerPortConfiguration = {}  # type: ignore[typeddict-item]
    if "ContainerPortRanges" in data:
        import aws_sdk_gamelift.types.container_port_range_list

        out["container_port_ranges"] = (
            aws_sdk_gamelift.types.container_port_range_list.deserialize_aws_json_1_1(
                data["ContainerPortRanges"]
            )
        )
    return out
