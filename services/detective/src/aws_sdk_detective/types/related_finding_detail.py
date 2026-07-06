"""Generated from Smithy shape ``com.amazonaws.detective#RelatedFindingDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_detective.types.entity_arn
    import aws_sdk_detective.types.ip_address
    import aws_sdk_detective.types.type


class RelatedFindingDetail(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_detective.types.entity_arn.EntityArn"]
    """<p>The Amazon Resource Name (ARN) of the related finding.</p>"""
    type: NotRequired["aws_sdk_detective.types.type.Type"]
    """<p>The type of finding.</p>"""
    ip_address: NotRequired["aws_sdk_detective.types.ip_address.IpAddress"]
    """<p>The IP address of the finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RelatedFindingDetail) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "type" in value:
        out["Type"] = value["type"]
    if "ip_address" in value:
        out["IpAddress"] = value["ip_address"]
    return out


def deserialize_json(data: dict) -> RelatedFindingDetail:
    out: RelatedFindingDetail = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "IpAddress" in data:
        out["ip_address"] = data["IpAddress"]
    return out
