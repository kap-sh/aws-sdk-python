"""Generated from Smithy shape ``com.amazonaws.gamelift#CreateContainerFleetOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.container_fleet


class CreateContainerFleetOutput(TypedDict):
    container_fleet: NotRequired[
        "aws_sdk_gamelift.types.container_fleet.ContainerFleet"
    ]
    """<p>The properties for the new container fleet, including current status. All fleets are initially placed in <code>PENDING</code> status. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateContainerFleetOutput) -> dict:
    out: dict = {}
    if "container_fleet" in value:
        import aws_sdk_gamelift.types.container_fleet

        out["ContainerFleet"] = (
            aws_sdk_gamelift.types.container_fleet.serialize_aws_json_1_1(
                value["container_fleet"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateContainerFleetOutput:
    out: CreateContainerFleetOutput = {}  # type: ignore[typeddict-item]
    if "ContainerFleet" in data:
        import aws_sdk_gamelift.types.container_fleet

        out["container_fleet"] = (
            aws_sdk_gamelift.types.container_fleet.deserialize_aws_json_1_1(
                data["ContainerFleet"]
            )
        )
    return out
