"""Generated from Smithy shape ``com.amazonaws.gamelift#UpdateContainerFleetOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.container_fleet


class UpdateContainerFleetOutput(TypedDict):
    container_fleet: NotRequired[
        "aws_sdk_gamelift.types.container_fleet.ContainerFleet"
    ]
    """<p>A collection of container fleet objects for all fleets that match the request criteria.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateContainerFleetOutput) -> dict:
    out: dict = {}
    if "container_fleet" in value:
        import aws_sdk_gamelift.types.container_fleet

        out["ContainerFleet"] = (
            aws_sdk_gamelift.types.container_fleet.serialize_aws_json_1_1(
                value["container_fleet"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateContainerFleetOutput:
    out: UpdateContainerFleetOutput = {}  # type: ignore[typeddict-item]
    if "ContainerFleet" in data:
        import aws_sdk_gamelift.types.container_fleet

        out["container_fleet"] = (
            aws_sdk_gamelift.types.container_fleet.deserialize_aws_json_1_1(
                data["ContainerFleet"]
            )
        )
    return out
