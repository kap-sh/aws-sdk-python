"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElbLoadBalancerSourceSecurityGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsElbLoadBalancerSourceSecurityGroup(TypedDict, closed=True):
    group_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the security group.</p>"""
    owner_alias: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The owner of the security group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsElbLoadBalancerSourceSecurityGroup) -> dict:
    out: dict = {}
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
    if "owner_alias" in value:
        out["OwnerAlias"] = value["owner_alias"]
    return out


def deserialize_json(data: dict) -> AwsElbLoadBalancerSourceSecurityGroup:
    out: AwsElbLoadBalancerSourceSecurityGroup = {}  # type: ignore[typeddict-item]
    if "GroupName" in data:
        out["group_name"] = data["GroupName"]
    if "OwnerAlias" in data:
        out["owner_alias"] = data["OwnerAlias"]
    return out
