"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2InstanceMonitoringDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEc2InstanceMonitoringDetails(TypedDict, closed=True):
    state: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> Indicates whether detailed monitoring is turned on. Otherwise, basic monitoring is turned on. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2InstanceMonitoringDetails) -> dict:
    out: dict = {}
    if "state" in value:
        out["State"] = value["state"]
    return out


def deserialize_json(data: dict) -> AwsEc2InstanceMonitoringDetails:
    out: AwsEc2InstanceMonitoringDetails = {}  # type: ignore[typeddict-item]
    if "State" in data:
        out["state"] = data["State"]
    return out
