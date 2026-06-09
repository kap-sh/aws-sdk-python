"""Generated from Smithy shape ``com.amazonaws.ec2#ResetAddressAttributeResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.address_attribute


class ResetAddressAttributeResult(TypedDict):
    address: NotRequired["aws_sdk_ec2.types.address_attribute.AddressAttribute"]
    """<p>Information about the IP address.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ResetAddressAttributeResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "address" in value:
        import aws_sdk_ec2.types.address_attribute

        aws_sdk_ec2.types.address_attribute.serialize_ec2_query(
            value["address"], pairs, f"{prefix}.Address"
        )


def deserialize_ec2_query(el: Element) -> ResetAddressAttributeResult:
    out: ResetAddressAttributeResult = {}  # type: ignore[typeddict-item]
    child_address = el.find("Address")
    if child_address is not None:
        import aws_sdk_ec2.types.address_attribute

        out["address"] = aws_sdk_ec2.types.address_attribute.deserialize_ec2_query(
            child_address
        )
    return out
