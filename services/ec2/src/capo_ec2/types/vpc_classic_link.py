"""Generated from Smithy shape ``com.amazonaws.ec2#VpcClassicLink``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class VpcClassicLink(TypedDict, closed=True):
    classic_link_enabled: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the VPC is enabled for ClassicLink.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the VPC.</p>"""
    vpc_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the VPC.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpcClassicLink, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "classic_link_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}ClassicLinkEnabled",
                "true" if value["classic_link_enabled"] else "false",
            )
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))


def deserialize_ec2_query(el: Element) -> VpcClassicLink:
    out: VpcClassicLink = {}  # type: ignore[typeddict-item]
    child_classic_link_enabled = el.find("classicLinkEnabled")
    if child_classic_link_enabled is not None:
        out["classic_link_enabled"] = (
            child_classic_link_enabled.text or ""
        ).lower() == "true"
    if el.find("tagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "tagSet")
    child_vpc_id = el.find("vpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    return out
