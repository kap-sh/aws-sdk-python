"""Generated from Smithy shape ``com.amazonaws.dax#SecurityGroupMembership``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dax.types.string


class SecurityGroupMembership(TypedDict, closed=True):
    security_group_identifier: NotRequired["aws_sdk_dax.types.string.String"]
    """<p>The unique ID for this security group.</p>"""
    status: NotRequired["aws_sdk_dax.types.string.String"]
    """<p>The status of this security group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecurityGroupMembership) -> dict:
    out: dict = {}
    if "security_group_identifier" in value:
        out["SecurityGroupIdentifier"] = value["security_group_identifier"]
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SecurityGroupMembership:
    out: SecurityGroupMembership = {}  # type: ignore[typeddict-item]
    if "SecurityGroupIdentifier" in data:
        out["security_group_identifier"] = data["SecurityGroupIdentifier"]
    if "Status" in data:
        out["status"] = data["Status"]
    return out
