"""Generated from Smithy shape ``com.amazonaws.s3#AnalyticsAndOperator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.prefix
    import aws_sdk_s3.types.tag_set


class AnalyticsAndOperator(TypedDict, closed=True):
    prefix: NotRequired["aws_sdk_s3.types.prefix.Prefix"]
    """<p>The prefix to use when evaluating an AND predicate: The prefix that an object must have to be included in the metrics results.</p>"""
    tags: NotRequired["aws_sdk_s3.types.tag_set.TagSet"]
    """<p>The list of tags to use when evaluating an AND predicate.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: AnalyticsAndOperator, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "prefix" in value:
        SubElement(el, "Prefix").text = str(value["prefix"])
    if "tags" in value:
        import aws_sdk_s3.types.tag_set

        aws_sdk_s3.types.tag_set.serialize_xml_flat(value["tags"], el, "Tag")


def deserialize_xml(el: Element) -> AnalyticsAndOperator:
    out: AnalyticsAndOperator = {}  # type: ignore[typeddict-item]
    child_prefix = el.find("Prefix")
    if child_prefix is not None:
        out["prefix"] = str(child_prefix.text or "")
    if el.find("Tag") is not None:
        import aws_sdk_s3.types.tag_set

        out["tags"] = aws_sdk_s3.types.tag_set.deserialize_xml_flat(el, "Tag")
    return out
