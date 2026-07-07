"""Generated from Smithy shape ``com.amazonaws.ec2#VpcClassicLink``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class VpcClassicLink(TypedDict, closed=True):
    classic_link_enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the VPC is enabled for ClassicLink.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the VPC.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpcClassicLink, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "classic_link_enabled" in value:
        pairs.append(
            (
                f"{prefix}.ClassicLinkEnabled",
                "true" if value["classic_link_enabled"] else "false",
            )
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))


def deserialize_ec2_query(el: Element) -> VpcClassicLink:
    out: VpcClassicLink = {}  # type: ignore[typeddict-item]
    child_classic_link_enabled = el.find("ClassicLinkEnabled")
    if child_classic_link_enabled is not None:
        out["classic_link_enabled"] = (
            child_classic_link_enabled.text or ""
        ).lower() == "true"
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    return out
