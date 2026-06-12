"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#SelfManageResources``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_migrationhubstrategy.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.self_manage_target_destinations


class SelfManageResources(TypedDict):
    target_destination: "aws_sdk_migrationhubstrategy.types.self_manage_target_destinations.SelfManageTargetDestinations"
    """<p> Self-managed resources target destination. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SelfManageResources) -> dict:
    out: dict = {}
    import aws_sdk_migrationhubstrategy.types.self_manage_target_destinations

    out["targetDestination"] = (
        aws_sdk_migrationhubstrategy.types.self_manage_target_destinations.serialize_json(
            value["target_destination"]
        )
    )
    return out


def deserialize_json(data: dict) -> SelfManageResources:
    out: SelfManageResources = {}  # type: ignore[typeddict-item]
    if "targetDestination" in data:
        import aws_sdk_migrationhubstrategy.types.self_manage_target_destinations

        out["target_destination"] = (
            aws_sdk_migrationhubstrategy.types.self_manage_target_destinations.deserialize_json(
                data["targetDestination"]
            )
        )
    else:
        raise DeserializationError("SelfManageResources.target_destination required")
    return out
