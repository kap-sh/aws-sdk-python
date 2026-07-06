"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPublicAddressTags``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_public_address_tag_list


class IpamPublicAddressTags(TypedDict, closed=True):
    eip_tags: NotRequired[
        "aws_sdk_ec2.types.ipam_public_address_tag_list.IpamPublicAddressTagList"
    ]
    """<p>Tags for an Elastic IP address.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPublicAddressTags, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "eip_tags" in value:
        import aws_sdk_ec2.types.ipam_public_address_tag_list

        aws_sdk_ec2.types.ipam_public_address_tag_list.serialize_ec2_query(
            value["eip_tags"], pairs, f"{prefix}.EipTagSet"
        )


def deserialize_ec2_query(el: Element) -> IpamPublicAddressTags:
    out: IpamPublicAddressTags = {}  # type: ignore[typeddict-item]
    if el.find("EipTagSet") is not None:
        import aws_sdk_ec2.types.ipam_public_address_tag_list

        out["eip_tags"] = (
            aws_sdk_ec2.types.ipam_public_address_tag_list.deserialize_ec2_query(
                el, "EipTagSet"
            )
        )
    return out
