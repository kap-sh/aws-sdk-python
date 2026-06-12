"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataMaintenanceOptionsDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEc2LaunchTemplateDataMaintenanceOptionsDetails(TypedDict):
    auto_recovery: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> Disables the automatic recovery behavior of your instance or sets it to default. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2LaunchTemplateDataMaintenanceOptionsDetails) -> dict:
    out: dict = {}
    if "auto_recovery" in value:
        out["AutoRecovery"] = value["auto_recovery"]
    return out


def deserialize_json(data: dict) -> AwsEc2LaunchTemplateDataMaintenanceOptionsDetails:
    out: AwsEc2LaunchTemplateDataMaintenanceOptionsDetails = {}  # type: ignore[typeddict-item]
    if "AutoRecovery" in data:
        out["auto_recovery"] = data["AutoRecovery"]
    return out
