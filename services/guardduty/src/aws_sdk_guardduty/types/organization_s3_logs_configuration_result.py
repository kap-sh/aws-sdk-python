"""Generated from Smithy shape ``com.amazonaws.guardduty#OrganizationS3LogsConfigurationResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.boolean


class OrganizationS3LogsConfigurationResult(TypedDict):
    auto_enable: NotRequired["aws_sdk_guardduty.types.boolean.Boolean"]
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
