"""Generated from Smithy shape ``com.amazonaws.guardduty#OrganizationEbsVolumesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.boolean


class OrganizationEbsVolumesResult(TypedDict, closed=True):
    auto_enable: NotRequired["capo_guardduty.types.boolean.Boolean"]
    """<p>An object that contains the status of whether scanning EBS volumes should be auto-enabled for new members joining the organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationEbsVolumesResult) -> dict:
    out: dict = {}
    if "auto_enable" in value:
        out["autoEnable"] = value["auto_enable"]
    return out


def deserialize_json(data: dict) -> OrganizationEbsVolumesResult:
    out: OrganizationEbsVolumesResult = {}  # type: ignore[typeddict-item]
    if "autoEnable" in data:
        out["auto_enable"] = data["autoEnable"]
    return out
