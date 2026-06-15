"""Generated from Smithy shape ``com.amazonaws.redshift#IPRange``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string
    import aws_sdk_redshift.types.tag_list


class IPRange(TypedDict):
    status: NotRequired["aws_sdk_redshift.types.string.String"]
    r"""<p>The status of the IP range, for example, \"authorized\".</p>"""
    cidrip: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The IP range in Classless Inter-Domain Routing (CIDR) notation.</p>"""
    tags: NotRequired["aws_sdk_redshift.types.tag_list.TagList"]
    """<p>The list of tags for the IP range.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: IPRange, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))
    if "cidrip" in value:
        pairs.append((f"{prefix}.CIDRIP", str(value["cidrip"])))
    if "tags" in value:
        import aws_sdk_redshift.types.tag_list

        aws_sdk_redshift.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> IPRange:
    out: IPRange = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_cidrip = el.find("CIDRIP")
    if child_cidrip is not None:
        out["cidrip"] = str(child_cidrip.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_redshift.types.tag_list

        out["tags"] = aws_sdk_redshift.types.tag_list.deserialize_query(child_tags)
    return out
