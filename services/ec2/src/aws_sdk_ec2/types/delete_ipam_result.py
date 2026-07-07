"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteIpamResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam


class DeleteIpamResult(TypedDict, closed=True):
    ipam: NotRequired["aws_sdk_ec2.types.ipam.Ipam"]
    """<p>Information about the results of the deletion.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteIpamResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ipam" in value:
        import aws_sdk_ec2.types.ipam

        aws_sdk_ec2.types.ipam.serialize_ec2_query(
            value["ipam"], pairs, f"{prefix}.Ipam"
        )


def deserialize_ec2_query(el: Element) -> DeleteIpamResult:
    out: DeleteIpamResult = {}  # type: ignore[typeddict-item]
    child_ipam = el.find("Ipam")
    if child_ipam is not None:
        import aws_sdk_ec2.types.ipam

        out["ipam"] = aws_sdk_ec2.types.ipam.deserialize_ec2_query(child_ipam)
    return out
