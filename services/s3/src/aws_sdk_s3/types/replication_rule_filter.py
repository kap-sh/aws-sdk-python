"""Generated from Smithy shape ``com.amazonaws.s3#ReplicationRuleFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.prefix
    import aws_sdk_s3.types.replication_rule_and_operator
    import aws_sdk_s3.types.tag

ReplicationRuleFilter = TypedDict(
    "ReplicationRuleFilter",
    {
        "prefix": NotRequired["aws_sdk_s3.types.prefix.Prefix"],
        "tag": NotRequired["aws_sdk_s3.types.tag.Tag"],
        "and": NotRequired[
            "aws_sdk_s3.types.replication_rule_and_operator.ReplicationRuleAndOperator"
        ],
    },
    closed=True,
)


# --- restXml ser/de ---
def serialize_xml(value: ReplicationRuleFilter, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "prefix" in value:
        SubElement(el, "Prefix").text = str(value["prefix"])
    if "tag" in value:
        import aws_sdk_s3.types.tag

        aws_sdk_s3.types.tag.serialize_xml(value["tag"], el, "Tag")
    if "and" in value:
        import aws_sdk_s3.types.replication_rule_and_operator

        aws_sdk_s3.types.replication_rule_and_operator.serialize_xml(
            value["and"], el, "And"
        )


def deserialize_xml(el: Element) -> ReplicationRuleFilter:
    out: ReplicationRuleFilter = {}  # type: ignore[typeddict-item]
    child_prefix = el.find("Prefix")
    if child_prefix is not None:
        out["prefix"] = str(child_prefix.text or "")
    child_tag = el.find("Tag")
    if child_tag is not None:
        import aws_sdk_s3.types.tag

        out["tag"] = aws_sdk_s3.types.tag.deserialize_xml(child_tag)
    child_and = el.find("And")
    if child_and is not None:
        import aws_sdk_s3.types.replication_rule_and_operator

        out["and"] = aws_sdk_s3.types.replication_rule_and_operator.deserialize_xml(
            child_and
        )
    return out
