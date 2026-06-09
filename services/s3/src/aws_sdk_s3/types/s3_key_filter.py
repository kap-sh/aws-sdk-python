"""Generated from Smithy shape ``com.amazonaws.s3#S3KeyFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.filter_rule_list


class S3KeyFilter(TypedDict):
    filter_rules: NotRequired["aws_sdk_s3.types.filter_rule_list.FilterRuleList"]


# --- restXml ser/de ---
def serialize_xml(value: S3KeyFilter, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "filter_rules" in value:
        import aws_sdk_s3.types.filter_rule_list

        aws_sdk_s3.types.filter_rule_list.serialize_xml_flat(
            value["filter_rules"], el, "FilterRule"
        )


def deserialize_xml(el: Element) -> S3KeyFilter:
    out: S3KeyFilter = {}  # type: ignore[typeddict-item]
    if el.find("FilterRule") is not None:
        import aws_sdk_s3.types.filter_rule_list

        out["filter_rules"] = aws_sdk_s3.types.filter_rule_list.deserialize_xml_flat(
            el, "FilterRule"
        )
    return out
