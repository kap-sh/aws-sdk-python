"""Generated from Smithy shape ``com.amazonaws.ec2#InternetGateway``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.internet_gateway_attachment_list
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class InternetGateway(TypedDict, closed=True):
    attachments: NotRequired[
        "capo_ec2.types.internet_gateway_attachment_list.InternetGatewayAttachmentList"
    ]
    """<p>Any VPCs attached to the internet gateway.</p>"""
    internet_gateway_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the internet gateway.</p>"""
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the internet gateway.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the internet gateway.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InternetGateway, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "attachments" in value:
        import capo_ec2.types.internet_gateway_attachment_list

        capo_ec2.types.internet_gateway_attachment_list.serialize_ec2_query(
            value["attachments"], pairs, f"{key_prefix}AttachmentSet"
        )
    if "internet_gateway_id" in value:
        pairs.append(
            (f"{key_prefix}InternetGatewayId", str(value["internet_gateway_id"]))
        )
    if "owner_id" in value:
        pairs.append((f"{key_prefix}OwnerId", str(value["owner_id"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )


def deserialize_ec2_query(el: Element) -> InternetGateway:
    out: InternetGateway = {}  # type: ignore[typeddict-item]
    child_attachments = el.find("attachmentSet")
    if child_attachments is not None:
        import capo_ec2.types.internet_gateway_attachment_list

        out["attachments"] = (
            capo_ec2.types.internet_gateway_attachment_list.deserialize_ec2_query(
                child_attachments
            )
        )
    child_internet_gateway_id = el.find("internetGatewayId")
    if child_internet_gateway_id is not None:
        out["internet_gateway_id"] = str(child_internet_gateway_id.text or "")
    child_owner_id = el.find("ownerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    return out
