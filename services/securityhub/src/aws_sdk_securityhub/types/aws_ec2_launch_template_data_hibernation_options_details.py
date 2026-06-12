"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataHibernationOptionsDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean


class AwsEc2LaunchTemplateDataHibernationOptionsDetails(TypedDict):
    configured: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
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
