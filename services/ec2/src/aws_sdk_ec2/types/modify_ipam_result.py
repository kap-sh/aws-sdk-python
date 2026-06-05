"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIpamResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam


class ModifyIpamResult(TypedDict):
    ipam: NotRequired["aws_sdk_ec2.types.ipam.Ipam"]
    """<p>The results of the modification.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyIpamResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ipam" in value:
        import aws_sdk_ec2.types.ipam

        aws_sdk_ec2.types.ipam.serialize_ec2_query(
            value["ipam"], pairs, f"{prefix}.Ipam"
        )


def deserialize_ec2_query(el: Element) -> ModifyIpamResult:
    out: ModifyIpamResult = {}  # type: ignore[typeddict-item]
    child_ipam = el.find("Ipam")
    if child_ipam is not None:
        import aws_sdk_ec2.types.ipam

        out["ipam"] = aws_sdk_ec2.types.ipam.deserialize_ec2_query(child_ipam)
    return out
