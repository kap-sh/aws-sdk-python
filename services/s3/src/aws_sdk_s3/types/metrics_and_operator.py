"""Generated from Smithy shape ``com.amazonaws.s3#MetricsAndOperator``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.access_point_arn
    import aws_sdk_s3.types.prefix
    import aws_sdk_s3.types.tag_set


class MetricsAndOperator(TypedDict):
    prefix: NotRequired["aws_sdk_s3.types.prefix.Prefix"]
    """<p>The prefix used when evaluating an AND predicate.</p>"""
    tags: NotRequired["aws_sdk_s3.types.tag_set.TagSet"]
    """<p>The list of tags used when evaluating an AND predicate.</p> <note> <p> <code>Tag</code> filters are not supported for directory buckets.</p> </note>"""
    access_point_arn: NotRequired["aws_sdk_s3.types.access_point_arn.AccessPointArn"]
    """<p>The access point ARN used when evaluating an <code>AND</code> predicate.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: MetricsAndOperator, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "prefix" in value:
        SubElement(el, "Prefix").text = str(value["prefix"])
    if "tags" in value:
        import aws_sdk_s3.types.tag_set

        aws_sdk_s3.types.tag_set.serialize_xml_flat(value["tags"], el, "Tag")
    if "access_point_arn" in value:
        SubElement(el, "AccessPointArn").text = str(value["access_point_arn"])


def deserialize_xml(el: Element) -> MetricsAndOperator:
    out: MetricsAndOperator = {}  # type: ignore[typeddict-item]
    child_prefix = el.find("Prefix")
    if child_prefix is not None:
        out["prefix"] = str(child_prefix.text or "")
    if el.find("Tag") is not None:
        import aws_sdk_s3.types.tag_set

        out["tags"] = aws_sdk_s3.types.tag_set.deserialize_xml_flat(el, "Tag")
    child_access_point_arn = el.find("AccessPointArn")
    if child_access_point_arn is not None:
        out["access_point_arn"] = str(child_access_point_arn.text or "")
    return out
