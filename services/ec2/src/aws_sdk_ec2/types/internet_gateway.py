"""Generated from Smithy shape ``com.amazonaws.ec2#InternetGateway``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.internet_gateway_attachment_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class InternetGateway(TypedDict, closed=True):
    attachments: NotRequired[
        "aws_sdk_ec2.types.internet_gateway_attachment_list.InternetGatewayAttachmentList"
    ]
    """<p>Any VPCs attached to the internet gateway.</p>"""
    internet_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the internet gateway.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the internet gateway.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the internet gateway.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InternetGateway, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "attachments" in value:
        import aws_sdk_ec2.types.internet_gateway_attachment_list

        aws_sdk_ec2.types.internet_gateway_attachment_list.serialize_ec2_query(
            value["attachments"], pairs, f"{prefix}.AttachmentSet"
        )
    if "internet_gateway_id" in value:
        pairs.append((f"{prefix}.InternetGatewayId", str(value["internet_gateway_id"])))
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> InternetGateway:
    out: InternetGateway = {}  # type: ignore[typeddict-item]
    if el.find("AttachmentSet") is not None:
        import aws_sdk_ec2.types.internet_gateway_attachment_list

        out["attachments"] = (
            aws_sdk_ec2.types.internet_gateway_attachment_list.deserialize_ec2_query(
                el, "AttachmentSet"
            )
        )
    child_internet_gateway_id = el.find("InternetGatewayId")
    if child_internet_gateway_id is not None:
        out["internet_gateway_id"] = str(child_internet_gateway_id.text or "")
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
