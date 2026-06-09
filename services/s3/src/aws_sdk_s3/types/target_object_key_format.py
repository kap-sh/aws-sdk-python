"""Generated from Smithy shape ``com.amazonaws.s3#TargetObjectKeyFormat``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.partitioned_prefix
    import aws_sdk_s3.types.simple_prefix


class TargetObjectKeyFormat(TypedDict):
    simple_prefix: NotRequired["aws_sdk_s3.types.simple_prefix.SimplePrefix"]
    """<p>To use the simple format for S3 keys for log objects. To specify SimplePrefix format, set SimplePrefix to {}.</p>"""
    partitioned_prefix: NotRequired[
        "aws_sdk_s3.types.partitioned_prefix.PartitionedPrefix"
    ]
    """<p>Partitioned S3 key for log objects.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: TargetObjectKeyFormat, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "simple_prefix" in value:
        import aws_sdk_s3.types.simple_prefix

        aws_sdk_s3.types.simple_prefix.serialize_xml(
            value["simple_prefix"], el, "SimplePrefix"
        )
    if "partitioned_prefix" in value:
        import aws_sdk_s3.types.partitioned_prefix

        aws_sdk_s3.types.partitioned_prefix.serialize_xml(
            value["partitioned_prefix"], el, "PartitionedPrefix"
        )


def deserialize_xml(el: Element) -> TargetObjectKeyFormat:
    out: TargetObjectKeyFormat = {}  # type: ignore[typeddict-item]
    child_simple_prefix = el.find("SimplePrefix")
    if child_simple_prefix is not None:
        import aws_sdk_s3.types.simple_prefix

        out["simple_prefix"] = aws_sdk_s3.types.simple_prefix.deserialize_xml(
            child_simple_prefix
        )
    child_partitioned_prefix = el.find("PartitionedPrefix")
    if child_partitioned_prefix is not None:
        import aws_sdk_s3.types.partitioned_prefix

        out["partitioned_prefix"] = aws_sdk_s3.types.partitioned_prefix.deserialize_xml(
            child_partitioned_prefix
        )
    return out
