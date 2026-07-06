"""Generated from Smithy shape ``com.amazonaws.securityhub#IcmpTypeCode``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer


class IcmpTypeCode(TypedDict, closed=True):
    code: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The ICMP code for which to deny or allow access. To deny or allow all codes, use the value <code>-1</code>.</p>"""
    type: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The ICMP type for which to deny or allow access. To deny or allow all types, use the value <code>-1</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IcmpTypeCode) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> IcmpTypeCode:
    out: IcmpTypeCode = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        out["code"] = data["Code"]
    if "Type" in data:
        out["type"] = data["Type"]
    return out
