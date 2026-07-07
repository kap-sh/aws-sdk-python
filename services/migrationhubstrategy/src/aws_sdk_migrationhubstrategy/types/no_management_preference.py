"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#NoManagementPreference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_migrationhubstrategy.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.no_preference_target_destinations


class NoManagementPreference(TypedDict, closed=True):
    target_destination: "aws_sdk_migrationhubstrategy.types.no_preference_target_destinations.NoPreferenceTargetDestinations"
    """<p> The choice of application destination that you specify. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NoManagementPreference) -> dict:
    out: dict = {}
    import aws_sdk_migrationhubstrategy.types.no_preference_target_destinations

    out["targetDestination"] = (
        aws_sdk_migrationhubstrategy.types.no_preference_target_destinations.serialize_json(
            value["target_destination"]
        )
    )
    return out


def deserialize_json(data: dict) -> NoManagementPreference:
    out: NoManagementPreference = {}  # type: ignore[typeddict-item]
    if "targetDestination" in data:
        import aws_sdk_migrationhubstrategy.types.no_preference_target_destinations

        out["target_destination"] = (
            aws_sdk_migrationhubstrategy.types.no_preference_target_destinations.deserialize_json(
                data["targetDestination"]
            )
        )
    else:
        raise DeserializationError("NoManagementPreference.target_destination required")
    return out
