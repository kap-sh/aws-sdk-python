"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#AwsManagedResources``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_migrationhubstrategy.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.aws_managed_target_destinations


class AwsManagedResources(TypedDict):
    target_destination: "aws_sdk_migrationhubstrategy.types.aws_managed_target_destinations.AwsManagedTargetDestinations"
    """<p> The choice of application destination that you specify. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsManagedResources) -> dict:
    out: dict = {}
    import aws_sdk_migrationhubstrategy.types.aws_managed_target_destinations

    out["targetDestination"] = (
        aws_sdk_migrationhubstrategy.types.aws_managed_target_destinations.serialize_json(
            value["target_destination"]
        )
    )
    return out


def deserialize_json(data: dict) -> AwsManagedResources:
    out: AwsManagedResources = {}  # type: ignore[typeddict-item]
    if "targetDestination" in data:
        import aws_sdk_migrationhubstrategy.types.aws_managed_target_destinations

        out["target_destination"] = (
            aws_sdk_migrationhubstrategy.types.aws_managed_target_destinations.deserialize_json(
                data["targetDestination"]
            )
        )
    else:
        raise DeserializationError("AwsManagedResources.target_destination required")
    return out
