"""Generated from Smithy shape ``com.amazonaws.guardduty#OrganizationS3LogsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.boolean


class OrganizationS3LogsConfiguration(TypedDict, closed=True):
    auto_enable: NotRequired["capo_guardduty.types.boolean.Boolean"]
    """<p>A value that contains information on whether S3 data event logs will be enabled automatically as a data source for the organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationS3LogsConfiguration) -> dict:
    out: dict = {}
    if "auto_enable" in value:
        out["autoEnable"] = value["auto_enable"]
    return out


def deserialize_json(data: dict) -> OrganizationS3LogsConfiguration:
    out: OrganizationS3LogsConfiguration = {}  # type: ignore[typeddict-item]
    if "autoEnable" in data:
        out["auto_enable"] = data["autoEnable"]
    return out
