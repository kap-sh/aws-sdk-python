"""Generated from Smithy shape ``com.amazonaws.ec2#EgressOnlyInternetGateway``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.egress_only_internet_gateway_id
    import capo_ec2.types.internet_gateway_attachment_list
    import capo_ec2.types.tag_list


class EgressOnlyInternetGateway(TypedDict, closed=True):
    attachments: NotRequired[
        "capo_ec2.types.internet_gateway_attachment_list.InternetGatewayAttachmentList"
    ]
    """<p>Information about the attachment of the egress-only internet gateway.</p>"""
    egress_only_internet_gateway_id: NotRequired[
        "capo_ec2.types.egress_only_internet_gateway_id.EgressOnlyInternetGatewayId"
    ]
    """<p>The ID of the egress-only internet gateway.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the egress-only internet gateway.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EgressOnlyInternetGateway, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "attachments" in value:
        import capo_ec2.types.internet_gateway_attachment_list

        capo_ec2.types.internet_gateway_attachment_list.serialize_ec2_query(
            value["attachments"], pairs, f"{key_prefix}AttachmentSet"
        )
    if "egress_only_internet_gateway_id" in value:
        pairs.append(
            (
                f"{key_prefix}EgressOnlyInternetGatewayId",
                str(value["egress_only_internet_gateway_id"]),
            )
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )


def deserialize_ec2_query(el: Element) -> EgressOnlyInternetGateway:
    out: EgressOnlyInternetGateway = {}  # type: ignore[typeddict-item]
    if el.find("AttachmentSet") is not None:
        import capo_ec2.types.internet_gateway_attachment_list

        out["attachments"] = (
            capo_ec2.types.internet_gateway_attachment_list.deserialize_ec2_query(
                el, "AttachmentSet"
            )
        )
    child_egress_only_internet_gateway_id = el.find("EgressOnlyInternetGatewayId")
    if child_egress_only_internet_gateway_id is not None:
        out["egress_only_internet_gateway_id"] = str(
            child_egress_only_internet_gateway_id.text or ""
        )
    if el.find("TagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
