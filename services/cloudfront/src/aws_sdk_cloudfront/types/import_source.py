"""Generated from Smithy shape ``com.amazonaws.cloudfront#ImportSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.import_source_type
    import aws_sdk_cloudfront.types.string


class ImportSource(TypedDict, closed=True):
    source_type: "aws_sdk_cloudfront.types.import_source_type.ImportSourceType"
    """<p>The source type of the import source for the key value store.</p>"""
    source_arn: "aws_sdk_cloudfront.types.string.string"
    """<p>The Amazon Resource Name (ARN) of the import source for the key value store.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ImportSource, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.import_source_type

    aws_sdk_cloudfront.types.import_source_type.serialize_xml(
        value["source_type"], el, "SourceType"
    )
    SubElement(el, "SourceARN").text = str(value["source_arn"])


def deserialize_xml(el: Element) -> ImportSource:
    out: ImportSource = {}  # type: ignore[typeddict-item]
    child_source_type = el.find("SourceType")
    if child_source_type is not None:
        import aws_sdk_cloudfront.types.import_source_type

        out["source_type"] = (
            aws_sdk_cloudfront.types.import_source_type.deserialize_xml(
                child_source_type
            )
        )
    else:
        raise DeserializationError("ImportSource.source_type required")
    child_source_arn = el.find("SourceARN")
    if child_source_arn is not None:
        out["source_arn"] = str(child_source_arn.text or "")
    else:
        raise DeserializationError("ImportSource.source_arn required")
    return out
