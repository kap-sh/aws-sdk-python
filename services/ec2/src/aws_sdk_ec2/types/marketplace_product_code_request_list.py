"""Generated from Smithy shape ``com.amazonaws.ec2#MarketplaceProductCodeRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.marketplace_product_code_request

MarketplaceProductCodeRequestList: TypeAlias = list[
    "aws_sdk_ec2.types.marketplace_product_code_request.MarketplaceProductCodeRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: MarketplaceProductCodeRequestList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_ec2_query(
    parent: Element, tag: str
) -> MarketplaceProductCodeRequestList:
    out: MarketplaceProductCodeRequestList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
