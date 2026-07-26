"""Generated from Smithy shape ``com.amazonaws.medialive#AutomaticInputFailoverSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min1
    import capo_medialive.types.__list_of_failover_condition
    import capo_medialive.types.__string
    import capo_medialive.types.input_preference


class AutomaticInputFailoverSettings(TypedDict, closed=True):
    error_clear_time_msec: NotRequired[
        "capo_medialive.types.__integer_min1.__integerMin1"
    ]
    """This clear time defines the requirement a recovered input must meet to be considered healthy. The input must have no failover conditions for this length of time. Enter a time in milliseconds. This value is particularly important if the input_preference for the failover pair is set to PRIMARY_INPUT_PREFERRED, because after this time, MediaLive will switch back to the primary input."""
    failover_conditions: NotRequired[
        "capo_medialive.types.__list_of_failover_condition.__listOfFailoverCondition"
    ]
    """A list of failover conditions. If any of these conditions occur, MediaLive will perform a failover to the other input."""
    input_preference: NotRequired[
        "capo_medialive.types.input_preference.InputPreference"
    ]
    """Input preference when deciding which input to make active when a previously failed input has recovered."""
    secondary_input_id: NotRequired["capo_medialive.types.__string.__string"]
    """The input ID of the secondary input in the automatic input failover pair."""


# --- restJson1 ser/de ---
def serialize_json(value: AutomaticInputFailoverSettings) -> dict:
    out: dict = {}
    if "error_clear_time_msec" in value:
        out["errorClearTimeMsec"] = value["error_clear_time_msec"]
    if "failover_conditions" in value:
        import capo_medialive.types.__list_of_failover_condition

        out["failoverConditions"] = (
            capo_medialive.types.__list_of_failover_condition.serialize_json(
                value["failover_conditions"]
            )
        )
    if "input_preference" in value:
        import capo_medialive.types.input_preference

        out["inputPreference"] = capo_medialive.types.input_preference.serialize_json(
            value["input_preference"]
        )
    if "secondary_input_id" in value:
        out["secondaryInputId"] = value["secondary_input_id"]
    return out


def deserialize_json(data: dict) -> AutomaticInputFailoverSettings:
    out: AutomaticInputFailoverSettings = {}  # type: ignore[typeddict-item]
    if "errorClearTimeMsec" in data:
        out["error_clear_time_msec"] = data["errorClearTimeMsec"]
    if "failoverConditions" in data:
        import capo_medialive.types.__list_of_failover_condition

        out["failover_conditions"] = (
            capo_medialive.types.__list_of_failover_condition.deserialize_json(
                data["failoverConditions"]
            )
        )
    if "inputPreference" in data:
        import capo_medialive.types.input_preference

        out["input_preference"] = (
            capo_medialive.types.input_preference.deserialize_json(
                data["inputPreference"]
            )
        )
    if "secondaryInputId" in data:
        out["secondary_input_id"] = data["secondaryInputId"]
    return out
