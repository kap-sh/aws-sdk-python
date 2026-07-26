"""Generated from Smithy shape ``com.amazonaws.finspace#IcmpTypeCode``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.icmp_type_or_code


class IcmpTypeCode(TypedDict, closed=True):
    type: "capo_finspace.types.icmp_type_or_code.IcmpTypeOrCode"
    """<p>The ICMP type. A value of <i>-1</i> means all types. </p>"""
    code: "capo_finspace.types.icmp_type_or_code.IcmpTypeOrCode"
    """<p> The ICMP code. A value of <i>-1</i> means all codes for the specified ICMP type. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IcmpTypeCode) -> dict:
    out: dict = {}
    out["type"] = value.get("type", 0)
    out["code"] = value.get("code", 0)
    return out


def deserialize_json(data: dict) -> IcmpTypeCode:
    out: IcmpTypeCode = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        out["type"] = 0
    if "code" in data:
        out["code"] = data["code"]
    else:
        out["code"] = 0
    return out
