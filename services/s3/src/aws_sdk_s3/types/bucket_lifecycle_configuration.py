"""Generated from Smithy shape ``com.amazonaws.s3#BucketLifecycleConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_s3.errors import DeserializationError
from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.lifecycle_rules


class BucketLifecycleConfiguration(TypedDict):
    rules: "aws_sdk_s3.types.lifecycle_rules.LifecycleRules"
    """<p>A lifecycle rule for individual objects in an Amazon S3 bucket.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: BucketLifecycleConfiguration, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3.types.lifecycle_rules

    aws_sdk_s3.types.lifecycle_rules.serialize_xml_flat(value["rules"], el, "Rule")


def deserialize_xml(el: Element) -> BucketLifecycleConfiguration:
    out: BucketLifecycleConfiguration = {}  # type: ignore[typeddict-item]
    if el.find("Rule") is not None:
        import aws_sdk_s3.types.lifecycle_rules

        out["rules"] = aws_sdk_s3.types.lifecycle_rules.deserialize_xml_flat(el, "Rule")
    else:
        raise DeserializationError("BucketLifecycleConfiguration.rules required")
    return out
