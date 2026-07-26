"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2NetworkInterfaceSecurityGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsEc2NetworkInterfaceSecurityGroup(TypedDict, closed=True):
    group_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the security group.</p>"""
    group_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the security group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2NetworkInterfaceSecurityGroup) -> dict:
    out: dict = {}
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
    if "group_id" in value:
        out["GroupId"] = value["group_id"]
    return out


def deserialize_json(data: dict) -> AwsEc2NetworkInterfaceSecurityGroup:
    out: AwsEc2NetworkInterfaceSecurityGroup = {}  # type: ignore[typeddict-item]
    if "GroupName" in data:
        out["group_name"] = data["GroupName"]
    if "GroupId" in data:
        out["group_id"] = data["GroupId"]
    return out
