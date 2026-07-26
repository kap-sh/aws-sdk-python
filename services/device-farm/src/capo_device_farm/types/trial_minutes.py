"""Generated from Smithy shape ``com.amazonaws.devicefarm#TrialMinutes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.double


class TrialMinutes(TypedDict, closed=True):
    total: NotRequired["capo_device_farm.types.double.Double"]
    """<p>The total number of free trial minutes that the account started with.</p>"""
    remaining: NotRequired["capo_device_farm.types.double.Double"]
    """<p>The number of free trial minutes remaining in the account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrialMinutes) -> dict:
    out: dict = {}
    if "total" in value:
        out["total"] = value["total"]
    if "remaining" in value:
        out["remaining"] = value["remaining"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TrialMinutes:
    out: TrialMinutes = {}  # type: ignore[typeddict-item]
    if "total" in data:
        out["total"] = data["total"]
    if "remaining" in data:
        out["remaining"] = data["remaining"]
    return out
