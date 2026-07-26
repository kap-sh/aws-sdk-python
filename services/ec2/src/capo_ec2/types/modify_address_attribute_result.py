"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyAddressAttributeResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.address_attribute


class ModifyAddressAttributeResult(TypedDict, closed=True):
    address: NotRequired["capo_ec2.types.address_attribute.AddressAttribute"]
    """<p>Information about the Elastic IP address.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyAddressAttributeResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "address" in value:
        import capo_ec2.types.address_attribute

        capo_ec2.types.address_attribute.serialize_ec2_query(
            value["address"], pairs, f"{prefix}.Address"
        )


def deserialize_ec2_query(el: Element) -> ModifyAddressAttributeResult:
    out: ModifyAddressAttributeResult = {}  # type: ignore[typeddict-item]
    child_address = el.find("Address")
    if child_address is not None:
        import capo_ec2.types.address_attribute

        out["address"] = capo_ec2.types.address_attribute.deserialize_ec2_query(
            child_address
        )
    return out
