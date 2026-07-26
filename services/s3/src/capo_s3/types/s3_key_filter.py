"""Generated from Smithy shape ``com.amazonaws.s3#S3KeyFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.filter_rule_list


class S3KeyFilter(TypedDict, closed=True):
    filter_rules: NotRequired["capo_s3.types.filter_rule_list.FilterRuleList"]


# --- restXml ser/de ---
def serialize_xml(value: S3KeyFilter, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "filter_rules" in value:
        import capo_s3.types.filter_rule_list

        capo_s3.types.filter_rule_list.serialize_xml_flat(
            value["filter_rules"], el, "FilterRule"
        )


def deserialize_xml(el: Element) -> S3KeyFilter:
    out: S3KeyFilter = {}  # type: ignore[typeddict-item]
    if el.find("FilterRule") is not None:
        import capo_s3.types.filter_rule_list

        out["filter_rules"] = capo_s3.types.filter_rule_list.deserialize_xml_flat(
            el, "FilterRule"
        )
    return out
