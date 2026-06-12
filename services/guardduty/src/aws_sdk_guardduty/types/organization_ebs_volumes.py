"""Generated from Smithy shape ``com.amazonaws.guardduty#OrganizationEbsVolumes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.boolean


class OrganizationEbsVolumes(TypedDict):
    auto_enable: NotRequired["aws_sdk_guardduty.types.boolean.Boolean"]
    """<p>Whether scanning EBS volumes should be auto-enabled for new members joining the organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationEbsVolumes) -> dict:
    out: dict = {}
    if "auto_enable" in value:
        out["autoEnable"] = value["auto_enable"]
    return out


def deserialize_json(data: dict) -> OrganizationEbsVolumes:
    out: OrganizationEbsVolumes = {}  # type: ignore[typeddict-item]
    if "autoEnable" in data:
        out["auto_enable"] = data["autoEnable"]
    return out
