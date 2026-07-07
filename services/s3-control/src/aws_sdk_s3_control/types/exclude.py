"""Generated from Smithy shape ``com.amazonaws.s3control#Exclude``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.buckets
    import aws_sdk_s3_control.types.regions


class Exclude(TypedDict, closed=True):
    buckets: NotRequired["aws_sdk_s3_control.types.buckets.Buckets"]
    """<p>A container for the S3 Storage Lens bucket excludes.</p>"""
    regions: NotRequired["aws_sdk_s3_control.types.regions.Regions"]
    """<p>A container for the S3 Storage Lens Region excludes.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Exclude, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "buckets" in value:
        import aws_sdk_s3_control.types.buckets

        aws_sdk_s3_control.types.buckets.serialize_xml(value["buckets"], el, "Buckets")
    if "regions" in value:
        import aws_sdk_s3_control.types.regions

        aws_sdk_s3_control.types.regions.serialize_xml(value["regions"], el, "Regions")


def deserialize_xml(el: Element) -> Exclude:
    out: Exclude = {}  # type: ignore[typeddict-item]
    child_buckets = el.find("Buckets")
    if child_buckets is not None:
        import aws_sdk_s3_control.types.buckets

        out["buckets"] = aws_sdk_s3_control.types.buckets.deserialize_xml(child_buckets)
    child_regions = el.find("Regions")
    if child_regions is not None:
        import aws_sdk_s3_control.types.regions

        out["regions"] = aws_sdk_s3_control.types.regions.deserialize_xml(child_regions)
    return out
