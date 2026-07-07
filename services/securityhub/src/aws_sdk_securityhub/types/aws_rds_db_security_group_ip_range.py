"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbSecurityGroupIpRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsRdsDbSecurityGroupIpRange(TypedDict, closed=True):
    cidr_ip: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Specifies the IP range.</p>"""
    status: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Specifies the status of the IP range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbSecurityGroupIpRange) -> dict:
    out: dict = {}
    if "cidr_ip" in value:
        out["CidrIp"] = value["cidr_ip"]
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> AwsRdsDbSecurityGroupIpRange:
    out: AwsRdsDbSecurityGroupIpRange = {}  # type: ignore[typeddict-item]
    if "CidrIp" in data:
        out["cidr_ip"] = data["CidrIp"]
    if "Status" in data:
        out["status"] = data["Status"]
    return out
