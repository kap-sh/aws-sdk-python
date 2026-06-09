"""Generated from Smithy shape ``com.amazonaws.ec2#IcmpTypeCode``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer


class IcmpTypeCode(TypedDict):
    code: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The ICMP code. A value of -1 means all codes for the specified ICMP type.</p>"""
    type: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The ICMP type. A value of -1 means all types.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IcmpTypeCode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "code" in value:
        pairs.append((f"{prefix}.Code", str(value["code"])))
    if "type" in value:
        pairs.append((f"{prefix}.Type", str(value["type"])))


def deserialize_ec2_query(el: Element) -> IcmpTypeCode:
    out: IcmpTypeCode = {}  # type: ignore[typeddict-item]
    child_code = el.find("Code")
    if child_code is not None:
        out["code"] = int(child_code.text or "")
    child_type = el.find("Type")
    if child_type is not None:
        out["type"] = int(child_type.text or "")
    return out
