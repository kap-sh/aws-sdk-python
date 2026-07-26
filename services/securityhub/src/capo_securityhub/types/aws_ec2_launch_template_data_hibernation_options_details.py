"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataHibernationOptionsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean


class AwsEc2LaunchTemplateDataHibernationOptionsDetails(TypedDict, closed=True):
    configured: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p> If you set this parameter to <code>true</code>, the instance is enabled for hibernation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2LaunchTemplateDataHibernationOptionsDetails) -> dict:
    out: dict = {}
    if "configured" in value:
        out["Configured"] = value["configured"]
    return out


def deserialize_json(data: dict) -> AwsEc2LaunchTemplateDataHibernationOptionsDetails:
    out: AwsEc2LaunchTemplateDataHibernationOptionsDetails = {}  # type: ignore[typeddict-item]
    if "Configured" in data:
        out["configured"] = data["Configured"]
    return out
