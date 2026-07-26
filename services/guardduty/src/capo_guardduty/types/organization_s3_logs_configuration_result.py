"""Generated from Smithy shape ``com.amazonaws.guardduty#OrganizationS3LogsConfigurationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.boolean


class OrganizationS3LogsConfigurationResult(TypedDict, closed=True):
    auto_enable: NotRequired["capo_guardduty.types.boolean.Boolean"]
    """<p>A value that describes whether S3 data event logs are automatically enabled for new members of the organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationS3LogsConfigurationResult) -> dict:
    out: dict = {}
    if "auto_enable" in value:
        out["autoEnable"] = value["auto_enable"]
    return out


def deserialize_json(data: dict) -> OrganizationS3LogsConfigurationResult:
    out: OrganizationS3LogsConfigurationResult = {}  # type: ignore[typeddict-item]
    if "autoEnable" in data:
        out["auto_enable"] = data["autoEnable"]
    return out
