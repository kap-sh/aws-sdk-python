"""Generated from Smithy shape ``com.amazonaws.s3control#ReplicationRuleAndOperator``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.prefix
    import aws_sdk_s3_control.types.s3_tag_set


class ReplicationRuleAndOperator(TypedDict):
    prefix: NotRequired["aws_sdk_s3_control.types.prefix.Prefix"]
    """<p>An object key name prefix that identifies the subset of objects that the rule applies to.</p>"""
    tags: NotRequired["aws_sdk_s3_control.types.s3_tag_set.S3TagSet"]
    """<p>An array of tags that contain key and value pairs.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ReplicationRuleAndOperator, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "prefix" in value:
        SubElement(el, "Prefix").text = str(value["prefix"])
    if "tags" in value:
        import aws_sdk_s3_control.types.s3_tag_set

        aws_sdk_s3_control.types.s3_tag_set.serialize_xml(value["tags"], el, "Tags")


def deserialize_xml(el: Element) -> ReplicationRuleAndOperator:
    out: ReplicationRuleAndOperator = {}  # type: ignore[typeddict-item]
    child_prefix = el.find("Prefix")
    if child_prefix is not None:
        out["prefix"] = str(child_prefix.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_s3_control.types.s3_tag_set

        out["tags"] = aws_sdk_s3_control.types.s3_tag_set.deserialize_xml(child_tags)
    return out
