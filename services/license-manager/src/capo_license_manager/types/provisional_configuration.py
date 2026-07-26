"""Generated from Smithy shape ``com.amazonaws.licensemanager#ProvisionalConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_license_manager.types.box_integer


class ProvisionalConfiguration(TypedDict, closed=True):
    max_time_to_live_in_minutes: "capo_license_manager.types.box_integer.BoxInteger"
    """<p>Maximum time for the provisional configuration, in minutes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisionalConfiguration) -> dict:
    out: dict = {}
    out["MaxTimeToLiveInMinutes"] = value["max_time_to_live_in_minutes"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProvisionalConfiguration:
    out: ProvisionalConfiguration = {}  # type: ignore[typeddict-item]
    if "MaxTimeToLiveInMinutes" in data:
        out["max_time_to_live_in_minutes"] = data["MaxTimeToLiveInMinutes"]
    else:
        raise DeserializationError(
            "ProvisionalConfiguration.max_time_to_live_in_minutes required"
        )
    return out
