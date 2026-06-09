"""Generated from Smithy shape ``com.amazonaws.ec2#DeprovisionIpamByoasnResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.byoasn


class DeprovisionIpamByoasnResult(TypedDict):
    byoasn: NotRequired["aws_sdk_ec2.types.byoasn.Byoasn"]
    """<p>An ASN and BYOIP CIDR association.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeprovisionIpamByoasnResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "byoasn" in value:
        import aws_sdk_ec2.types.byoasn

        aws_sdk_ec2.types.byoasn.serialize_ec2_query(
            value["byoasn"], pairs, f"{prefix}.Byoasn"
        )


def deserialize_ec2_query(el: Element) -> DeprovisionIpamByoasnResult:
    out: DeprovisionIpamByoasnResult = {}  # type: ignore[typeddict-item]
    child_byoasn = el.find("Byoasn")
    if child_byoasn is not None:
        import aws_sdk_ec2.types.byoasn

        out["byoasn"] = aws_sdk_ec2.types.byoasn.deserialize_ec2_query(child_byoasn)
    return out
