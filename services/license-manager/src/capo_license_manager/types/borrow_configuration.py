"""Generated from Smithy shape ``com.amazonaws.licensemanager#BorrowConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_license_manager.types.box_boolean
    import capo_license_manager.types.box_integer


class BorrowConfiguration(TypedDict, closed=True):
    allow_early_check_in: "capo_license_manager.types.box_boolean.BoxBoolean"
    """<p>Indicates whether early check-ins are allowed.</p>"""
    max_time_to_live_in_minutes: "capo_license_manager.types.box_integer.BoxInteger"
    """<p>Maximum time for the borrow configuration, in minutes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BorrowConfiguration) -> dict:
    out: dict = {}
    out["AllowEarlyCheckIn"] = value["allow_early_check_in"]
    out["MaxTimeToLiveInMinutes"] = value["max_time_to_live_in_minutes"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BorrowConfiguration:
    out: BorrowConfiguration = {}  # type: ignore[typeddict-item]
    if "AllowEarlyCheckIn" in data:
        out["allow_early_check_in"] = data["AllowEarlyCheckIn"]
    else:
        raise DeserializationError("BorrowConfiguration.allow_early_check_in required")
    if "MaxTimeToLiveInMinutes" in data:
        out["max_time_to_live_in_minutes"] = data["MaxTimeToLiveInMinutes"]
    else:
        raise DeserializationError(
            "BorrowConfiguration.max_time_to_live_in_minutes required"
        )
    return out
