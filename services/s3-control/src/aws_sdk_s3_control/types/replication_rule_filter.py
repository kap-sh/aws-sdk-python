"""Generated from Smithy shape ``com.amazonaws.s3control#ReplicationRuleFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.prefix
    import aws_sdk_s3_control.types.replication_rule_and_operator
    import aws_sdk_s3_control.types.s3_tag

ReplicationRuleFilter = TypedDict(
    "ReplicationRuleFilter",
    {
        "prefix": NotRequired["aws_sdk_s3_control.types.prefix.Prefix"],
        "tag": NotRequired["aws_sdk_s3_control.types.s3_tag.S3Tag"],
        "and": NotRequired[
            "aws_sdk_s3_control.types.replication_rule_and_operator.ReplicationRuleAndOperator"
        ],
    },
)


# --- restXml ser/de ---
def serialize_xml(value: ReplicationRuleFilter, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "prefix" in value:
        SubElement(el, "Prefix").text = str(value["prefix"])
    if "tag" in value:
        import aws_sdk_s3_control.types.s3_tag

        aws_sdk_s3_control.types.s3_tag.serialize_xml(value["tag"], el, "Tag")
    if "and" in value:
        import aws_sdk_s3_control.types.replication_rule_and_operator

        aws_sdk_s3_control.types.replication_rule_and_operator.serialize_xml(
            value["and"], el, "And"
        )


def deserialize_xml(el: Element) -> ReplicationRuleFilter:
    out: ReplicationRuleFilter = {}  # type: ignore[typeddict-item]
    child_prefix = el.find("Prefix")
    if child_prefix is not None:
        out["prefix"] = str(child_prefix.text or "")
    child_tag = el.find("Tag")
    if child_tag is not None:
        import aws_sdk_s3_control.types.s3_tag

        out["tag"] = aws_sdk_s3_control.types.s3_tag.deserialize_xml(child_tag)
    child_and = el.find("And")
    if child_and is not None:
        import aws_sdk_s3_control.types.replication_rule_and_operator

        out["and"] = (
            aws_sdk_s3_control.types.replication_rule_and_operator.deserialize_xml(
                child_and
            )
        )
    return out
