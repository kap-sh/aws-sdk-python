"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPublicAddressTags``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_public_address_tag_list


class IpamPublicAddressTags(TypedDict, closed=True):
    eip_tags: NotRequired[
        "capo_ec2.types.ipam_public_address_tag_list.IpamPublicAddressTagList"
    ]
    """<p>Tags for an Elastic IP address.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPublicAddressTags, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "eip_tags" in value:
        import capo_ec2.types.ipam_public_address_tag_list

        capo_ec2.types.ipam_public_address_tag_list.serialize_ec2_query(
            value["eip_tags"], pairs, f"{prefix}.EipTagSet"
        )


def deserialize_ec2_query(el: Element) -> IpamPublicAddressTags:
    out: IpamPublicAddressTags = {}  # type: ignore[typeddict-item]
    if el.find("EipTagSet") is not None:
        import capo_ec2.types.ipam_public_address_tag_list

        out["eip_tags"] = (
            capo_ec2.types.ipam_public_address_tag_list.deserialize_ec2_query(
                el, "EipTagSet"
            )
        )
    return out
