"""Generated from Smithy shape ``com.amazonaws.s3control#LifecycleRuleFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.lifecycle_rule_and_operator
    import aws_sdk_s3_control.types.object_size_greater_than_bytes
    import aws_sdk_s3_control.types.object_size_less_than_bytes
    import aws_sdk_s3_control.types.prefix
    import aws_sdk_s3_control.types.s3_tag

LifecycleRuleFilter = TypedDict(
    "LifecycleRuleFilter",
    {
        "prefix": NotRequired["aws_sdk_s3_control.types.prefix.Prefix"],
        "tag": NotRequired["aws_sdk_s3_control.types.s3_tag.S3Tag"],
        "and": NotRequired[
            "aws_sdk_s3_control.types.lifecycle_rule_and_operator.LifecycleRuleAndOperator"
        ],
        "object_size_greater_than": NotRequired[
            "aws_sdk_s3_control.types.object_size_greater_than_bytes.ObjectSizeGreaterThanBytes"
        ],
        "object_size_less_than": NotRequired[
            "aws_sdk_s3_control.types.object_size_less_than_bytes.ObjectSizeLessThanBytes"
        ],
    },
    closed=True,
)


# --- restXml ser/de ---
def serialize_xml(value: LifecycleRuleFilter, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "prefix" in value:
        SubElement(el, "Prefix").text = str(value["prefix"])
    if "tag" in value:
        import aws_sdk_s3_control.types.s3_tag

        aws_sdk_s3_control.types.s3_tag.serialize_xml(value["tag"], el, "Tag")
    if "and" in value:
        import aws_sdk_s3_control.types.lifecycle_rule_and_operator

        aws_sdk_s3_control.types.lifecycle_rule_and_operator.serialize_xml(
            value["and"], el, "And"
        )
    if "object_size_greater_than" in value:
        SubElement(el, "ObjectSizeGreaterThan").text = str(
            value["object_size_greater_than"]
        )
    if "object_size_less_than" in value:
        SubElement(el, "ObjectSizeLessThan").text = str(value["object_size_less_than"])


def deserialize_xml(el: Element) -> LifecycleRuleFilter:
    out: LifecycleRuleFilter = {}  # type: ignore[typeddict-item]
    child_prefix = el.find("Prefix")
    if child_prefix is not None:
        out["prefix"] = str(child_prefix.text or "")
    child_tag = el.find("Tag")
    if child_tag is not None:
        import aws_sdk_s3_control.types.s3_tag

        out["tag"] = aws_sdk_s3_control.types.s3_tag.deserialize_xml(child_tag)
    child_and = el.find("And")
    if child_and is not None:
        import aws_sdk_s3_control.types.lifecycle_rule_and_operator

        out["and"] = (
            aws_sdk_s3_control.types.lifecycle_rule_and_operator.deserialize_xml(
                child_and
            )
        )
    child_object_size_greater_than = el.find("ObjectSizeGreaterThan")
    if child_object_size_greater_than is not None:
        out["object_size_greater_than"] = int(child_object_size_greater_than.text or "")
    child_object_size_less_than = el.find("ObjectSizeLessThan")
    if child_object_size_less_than is not None:
        out["object_size_less_than"] = int(child_object_size_less_than.text or "")
    return out
