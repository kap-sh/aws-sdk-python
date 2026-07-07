"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbInstanceEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class AwsRdsDbInstanceEndpoint(TypedDict, closed=True):
    address: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Specifies the DNS address of the DB instance.</p>"""
    port: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>Specifies the port that the database engine is listening on.</p>"""
    hosted_zone_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbInstanceEndpoint) -> dict:
    out: dict = {}
    if "address" in value:
        out["Address"] = value["address"]
    if "port" in value:
        out["Port"] = value["port"]
    if "hosted_zone_id" in value:
        out["HostedZoneId"] = value["hosted_zone_id"]
    return out


def deserialize_json(data: dict) -> AwsRdsDbInstanceEndpoint:
    out: AwsRdsDbInstanceEndpoint = {}  # type: ignore[typeddict-item]
    if "Address" in data:
        out["address"] = data["Address"]
    if "Port" in data:
        out["port"] = data["Port"]
    if "HostedZoneId" in data:
        out["hosted_zone_id"] = data["HostedZoneId"]
    return out
