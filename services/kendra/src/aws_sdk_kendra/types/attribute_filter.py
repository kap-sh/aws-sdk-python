"""Generated from Smithy shape ``com.amazonaws.kendra#AttributeFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.attribute_filter
    import aws_sdk_kendra.types.attribute_filter_list
    import aws_sdk_kendra.types.document_attribute


class AttributeFilter(TypedDict):
    and_all_filters: NotRequired[
        "aws_sdk_kendra.types.attribute_filter_list.AttributeFilterList"
    ]
    """<p>Performs a logical <code>AND</code> operation on all filters that you specify.</p>"""
    or_all_filters: NotRequired[
        "aws_sdk_kendra.types.attribute_filter_list.AttributeFilterList"
    ]
    """<p>Performs a logical <code>OR</code> operation on all filters that you specify.</p>"""
    not_filter: NotRequired["aws_sdk_kendra.types.attribute_filter.AttributeFilter"]
    """<p>Performs a logical <code>NOT</code> operation on all filters that you specify.</p>"""
    equals_to: NotRequired["aws_sdk_kendra.types.document_attribute.DocumentAttribute"]
    """<p>Performs an equals operation on document attributes/fields and their values.</p>"""
    contains_all: NotRequired[
        "aws_sdk_kendra.types.document_attribute.DocumentAttribute"
    ]
    """<p>Returns true when a document contains all of the specified document attributes/fields. This filter is only applicable to <a href=\"https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html\">StringListValue</a>.</p>"""
    contains_any: NotRequired[
        "aws_sdk_kendra.types.document_attribute.DocumentAttribute"
    ]
    """<p>Returns true when a document contains any of the specified document attributes/fields. This filter is only applicable to <a href=\"https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html\">StringListValue</a>.</p>"""
    greater_than: NotRequired[
        "aws_sdk_kendra.types.document_attribute.DocumentAttribute"
    ]
    """<p>Performs a greater than operation on document attributes/fields and their values. Use with the <a href=\"https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html\">document attribute type</a> <code>Date</code> or <code>Long</code>.</p>"""
    greater_than_or_equals: NotRequired[
        "aws_sdk_kendra.types.document_attribute.DocumentAttribute"
    ]
    """<p>Performs a greater or equals than operation on document attributes/fields and their values. Use with the <a href=\"https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html\">document attribute type</a> <code>Date</code> or <code>Long</code>.</p>"""
    less_than: NotRequired["aws_sdk_kendra.types.document_attribute.DocumentAttribute"]
    """<p>Performs a less than operation on document attributes/fields and their values. Use with the <a href=\"https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html\">document attribute type</a> <code>Date</code> or <code>Long</code>.</p>"""
    less_than_or_equals: NotRequired[
        "aws_sdk_kendra.types.document_attribute.DocumentAttribute"
    ]
    """<p>Performs a less than or equals operation on document attributes/fields and their values. Use with the <a href=\"https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html\">document attribute type</a> <code>Date</code> or <code>Long</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttributeFilter) -> dict:
    out: dict = {}
    if "and_all_filters" in value:
        import aws_sdk_kendra.types.attribute_filter_list

        out["AndAllFilters"] = (
            aws_sdk_kendra.types.attribute_filter_list.serialize_aws_json_1_1(
                value["and_all_filters"]
            )
        )
    if "or_all_filters" in value:
        import aws_sdk_kendra.types.attribute_filter_list

        out["OrAllFilters"] = (
            aws_sdk_kendra.types.attribute_filter_list.serialize_aws_json_1_1(
                value["or_all_filters"]
            )
        )
    if "not_filter" in value:
        import aws_sdk_kendra.types.attribute_filter

        out["NotFilter"] = aws_sdk_kendra.types.attribute_filter.serialize_aws_json_1_1(
            value["not_filter"]
        )
    if "equals_to" in value:
        import aws_sdk_kendra.types.document_attribute

        out["EqualsTo"] = (
            aws_sdk_kendra.types.document_attribute.serialize_aws_json_1_1(
                value["equals_to"]
            )
        )
    if "contains_all" in value:
        import aws_sdk_kendra.types.document_attribute

        out["ContainsAll"] = (
            aws_sdk_kendra.types.document_attribute.serialize_aws_json_1_1(
                value["contains_all"]
            )
        )
    if "contains_any" in value:
        import aws_sdk_kendra.types.document_attribute

        out["ContainsAny"] = (
            aws_sdk_kendra.types.document_attribute.serialize_aws_json_1_1(
                value["contains_any"]
            )
        )
    if "greater_than" in value:
        import aws_sdk_kendra.types.document_attribute

        out["GreaterThan"] = (
            aws_sdk_kendra.types.document_attribute.serialize_aws_json_1_1(
                value["greater_than"]
            )
        )
    if "greater_than_or_equals" in value:
        import aws_sdk_kendra.types.document_attribute

        out["GreaterThanOrEquals"] = (
            aws_sdk_kendra.types.document_attribute.serialize_aws_json_1_1(
                value["greater_than_or_equals"]
            )
        )
    if "less_than" in value:
        import aws_sdk_kendra.types.document_attribute

        out["LessThan"] = (
            aws_sdk_kendra.types.document_attribute.serialize_aws_json_1_1(
                value["less_than"]
            )
        )
    if "less_than_or_equals" in value:
        import aws_sdk_kendra.types.document_attribute

        out["LessThanOrEquals"] = (
            aws_sdk_kendra.types.document_attribute.serialize_aws_json_1_1(
                value["less_than_or_equals"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AttributeFilter:
    out: AttributeFilter = {}  # type: ignore[typeddict-item]
    if "AndAllFilters" in data:
        import aws_sdk_kendra.types.attribute_filter_list

        out["and_all_filters"] = (
            aws_sdk_kendra.types.attribute_filter_list.deserialize_aws_json_1_1(
                data["AndAllFilters"]
            )
        )
    if "OrAllFilters" in data:
        import aws_sdk_kendra.types.attribute_filter_list

        out["or_all_filters"] = (
            aws_sdk_kendra.types.attribute_filter_list.deserialize_aws_json_1_1(
                data["OrAllFilters"]
            )
        )
    if "NotFilter" in data:
        import aws_sdk_kendra.types.attribute_filter

        out["not_filter"] = (
            aws_sdk_kendra.types.attribute_filter.deserialize_aws_json_1_1(
                data["NotFilter"]
            )
        )
    if "EqualsTo" in data:
        import aws_sdk_kendra.types.document_attribute

        out["equals_to"] = (
            aws_sdk_kendra.types.document_attribute.deserialize_aws_json_1_1(
                data["EqualsTo"]
            )
        )
    if "ContainsAll" in data:
        import aws_sdk_kendra.types.document_attribute

        out["contains_all"] = (
            aws_sdk_kendra.types.document_attribute.deserialize_aws_json_1_1(
                data["ContainsAll"]
            )
        )
    if "ContainsAny" in data:
        import aws_sdk_kendra.types.document_attribute

        out["contains_any"] = (
            aws_sdk_kendra.types.document_attribute.deserialize_aws_json_1_1(
                data["ContainsAny"]
            )
        )
    if "GreaterThan" in data:
        import aws_sdk_kendra.types.document_attribute

        out["greater_than"] = (
            aws_sdk_kendra.types.document_attribute.deserialize_aws_json_1_1(
                data["GreaterThan"]
            )
        )
    if "GreaterThanOrEquals" in data:
        import aws_sdk_kendra.types.document_attribute

        out["greater_than_or_equals"] = (
            aws_sdk_kendra.types.document_attribute.deserialize_aws_json_1_1(
                data["GreaterThanOrEquals"]
            )
        )
    if "LessThan" in data:
        import aws_sdk_kendra.types.document_attribute

        out["less_than"] = (
            aws_sdk_kendra.types.document_attribute.deserialize_aws_json_1_1(
                data["LessThan"]
            )
        )
    if "LessThanOrEquals" in data:
        import aws_sdk_kendra.types.document_attribute

        out["less_than_or_equals"] = (
            aws_sdk_kendra.types.document_attribute.deserialize_aws_json_1_1(
                data["LessThanOrEquals"]
            )
        )
    return out
