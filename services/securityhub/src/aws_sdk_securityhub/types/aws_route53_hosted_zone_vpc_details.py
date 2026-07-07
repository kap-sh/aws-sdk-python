"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRoute53HostedZoneVpcDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsRoute53HostedZoneVpcDetails(TypedDict, closed=True):
    id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The identifier of an Amazon VPC. </p>"""
    region: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The Amazon Web Services Region that an Amazon VPC was created in.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRoute53HostedZoneVpcDetails) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "region" in value:
        out["Region"] = value["region"]
    return out


def deserialize_json(data: dict) -> AwsRoute53HostedZoneVpcDetails:
    out: AwsRoute53HostedZoneVpcDetails = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Region" in data:
        out["region"] = data["Region"]
    return out
