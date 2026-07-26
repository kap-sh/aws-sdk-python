"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeContainerFleetOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.container_fleet


class DescribeContainerFleetOutput(TypedDict, closed=True):
    container_fleet: NotRequired["capo_gamelift.types.container_fleet.ContainerFleet"]
    """<p>The properties for the requested container fleet, including current status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeContainerFleetOutput) -> dict:
    out: dict = {}
    if "container_fleet" in value:
        import capo_gamelift.types.container_fleet

        out["ContainerFleet"] = (
            capo_gamelift.types.container_fleet.serialize_aws_json_1_1(
                value["container_fleet"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeContainerFleetOutput:
    out: DescribeContainerFleetOutput = {}  # type: ignore[typeddict-item]
    if "ContainerFleet" in data:
        import capo_gamelift.types.container_fleet

        out["container_fleet"] = (
            capo_gamelift.types.container_fleet.deserialize_aws_json_1_1(
                data["ContainerFleet"]
            )
        )
    return out
