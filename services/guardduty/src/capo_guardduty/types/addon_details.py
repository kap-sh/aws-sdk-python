"""Generated from Smithy shape ``com.amazonaws.guardduty#AddonDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string


class AddonDetails(TypedDict, closed=True):
    addon_version: NotRequired["capo_guardduty.types.string.String"]
    """<p>Version of the installed EKS add-on.</p>"""
    addon_status: NotRequired["capo_guardduty.types.string.String"]
    """<p>Status of the installed EKS add-on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddonDetails) -> dict:
    out: dict = {}
    if "addon_version" in value:
        out["addonVersion"] = value["addon_version"]
    if "addon_status" in value:
        out["addonStatus"] = value["addon_status"]
    return out


def deserialize_json(data: dict) -> AddonDetails:
    out: AddonDetails = {}  # type: ignore[typeddict-item]
    if "addonVersion" in data:
        out["addon_version"] = data["addonVersion"]
    if "addonStatus" in data:
        out["addon_status"] = data["addonStatus"]
    return out
