"""Generated from Smithy shape ``com.amazonaws.qbusiness#AttributeFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.attribute_filter
    import aws_sdk_qbusiness.types.attribute_filters
    import aws_sdk_qbusiness.types.document_attribute


class AttributeFilter(TypedDict):
    and_all_filters: NotRequired[
        "aws_sdk_qbusiness.types.attribute_filters.AttributeFilters"
    ]
    """<p>Performs a logical <code>AND</code> operation on all supplied filters.</p>"""
    or_all_filters: NotRequired[
        "aws_sdk_qbusiness.types.attribute_filters.AttributeFilters"
    ]
    """<p> Performs a logical <code>OR</code> operation on all supplied filters. </p>"""
    not_filter: NotRequired["aws_sdk_qbusiness.types.attribute_filter.AttributeFilter"]
    """<p>Performs a logical <code>NOT</code> operation on all supplied filters. </p>"""
    equals_to: NotRequired[
        "aws_sdk_qbusiness.types.document_attribute.DocumentAttribute"
    ]
    """<p>Performs an equals operation on two document attributes or metadata fields. Supported for the following <a href=\"https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html\">document attribute value types</a>: <code>dateValue</code>, <code>longValue</code>, <code>stringListValue</code> and <code>stringValue</code>.</p>"""
    contains_all: NotRequired[
        "aws_sdk_qbusiness.types.document_attribute.DocumentAttribute"
    ]
    """<p>Returns <code>true</code> when a document contains all the specified document attributes or metadata fields. Supported for the following <a href=\"https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html\">document attribute value types</a>: <code>stringListValue</code>.</p>"""
    contains_any: NotRequired[
        "aws_sdk_qbusiness.types.document_attribute.DocumentAttribute"
    ]
    """<p>Returns <code>true</code> when a document contains any of the specified document attributes or metadata fields. Supported for the following <a href=\"https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html\">document attribute value types</a>: <code>stringListValue</code>.</p>"""
    greater_than: NotRequired[
        "aws_sdk_qbusiness.types.document_attribute.DocumentAttribute"
    ]
    """<p>Performs a greater than operation on two document attributes or metadata fields. Supported for the following <a href=\"https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html\">document attribute value types</a>: <code>dateValue</code> and <code>longValue</code>.</p>"""
    greater_than_or_equals: NotRequired[
        "aws_sdk_qbusiness.types.document_attribute.DocumentAttribute"
    ]
    """<p>Performs a greater or equals than operation on two document attributes or metadata fields. Supported for the following <a href=\"https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html\">document attribute value types</a>: <code>dateValue</code> and <code>longValue</code>. </p>"""
    less_than: NotRequired[
        "aws_sdk_qbusiness.types.document_attribute.DocumentAttribute"
    ]
    """<p>Performs a less than operation on two document attributes or metadata fields. Supported for the following <a href=\"https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html\">document attribute value types</a>: <code>dateValue</code> and <code>longValue</code>.</p>"""
    less_than_or_equals: NotRequired[
        "aws_sdk_qbusiness.types.document_attribute.DocumentAttribute"
    ]
    """<p>Performs a less than or equals operation on two document attributes or metadata fields.Supported for the following <a href=\"https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html\">document attribute value type</a>: <code>dateValue</code> and <code>longValue</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttributeFilter) -> dict:
    out: dict = {}
    if "and_all_filters" in value:
        import aws_sdk_qbusiness.types.attribute_filters

        out["andAllFilters"] = aws_sdk_qbusiness.types.attribute_filters.serialize_json(
            value["and_all_filters"]
        )
    if "or_all_filters" in value:
        import aws_sdk_qbusiness.types.attribute_filters

        out["orAllFilters"] = aws_sdk_qbusiness.types.attribute_filters.serialize_json(
            value["or_all_filters"]
        )
    if "not_filter" in value:
        import aws_sdk_qbusiness.types.attribute_filter

        out["notFilter"] = aws_sdk_qbusiness.types.attribute_filter.serialize_json(
            value["not_filter"]
        )
    if "equals_to" in value:
        import aws_sdk_qbusiness.types.document_attribute

        out["equalsTo"] = aws_sdk_qbusiness.types.document_attribute.serialize_json(
            value["equals_to"]
        )
    if "contains_all" in value:
        import aws_sdk_qbusiness.types.document_attribute

        out["containsAll"] = aws_sdk_qbusiness.types.document_attribute.serialize_json(
            value["contains_all"]
        )
    if "contains_any" in value:
        import aws_sdk_qbusiness.types.document_attribute

        out["containsAny"] = aws_sdk_qbusiness.types.document_attribute.serialize_json(
            value["contains_any"]
        )
    if "greater_than" in value:
        import aws_sdk_qbusiness.types.document_attribute

        out["greaterThan"] = aws_sdk_qbusiness.types.document_attribute.serialize_json(
            value["greater_than"]
        )
    if "greater_than_or_equals" in value:
        import aws_sdk_qbusiness.types.document_attribute

        out["greaterThanOrEquals"] = (
            aws_sdk_qbusiness.types.document_attribute.serialize_json(
                value["greater_than_or_equals"]
            )
        )
    if "less_than" in value:
        import aws_sdk_qbusiness.types.document_attribute

        out["lessThan"] = aws_sdk_qbusiness.types.document_attribute.serialize_json(
            value["less_than"]
        )
    if "less_than_or_equals" in value:
        import aws_sdk_qbusiness.types.document_attribute

        out["lessThanOrEquals"] = (
            aws_sdk_qbusiness.types.document_attribute.serialize_json(
                value["less_than_or_equals"]
            )
        )
    return out


def deserialize_json(data: dict) -> AttributeFilter:
    out: AttributeFilter = {}  # type: ignore[typeddict-item]
    if "andAllFilters" in data:
        import aws_sdk_qbusiness.types.attribute_filters

        out["and_all_filters"] = (
            aws_sdk_qbusiness.types.attribute_filters.deserialize_json(
                data["andAllFilters"]
            )
        )
    if "orAllFilters" in data:
        import aws_sdk_qbusiness.types.attribute_filters

        out["or_all_filters"] = (
            aws_sdk_qbusiness.types.attribute_filters.deserialize_json(
                data["orAllFilters"]
            )
        )
    if "notFilter" in data:
        import aws_sdk_qbusiness.types.attribute_filter

        out["not_filter"] = aws_sdk_qbusiness.types.attribute_filter.deserialize_json(
            data["notFilter"]
        )
    if "equalsTo" in data:
        import aws_sdk_qbusiness.types.document_attribute

        out["equals_to"] = aws_sdk_qbusiness.types.document_attribute.deserialize_json(
            data["equalsTo"]
        )
    if "containsAll" in data:
        import aws_sdk_qbusiness.types.document_attribute

        out["contains_all"] = (
            aws_sdk_qbusiness.types.document_attribute.deserialize_json(
                data["containsAll"]
            )
        )
    if "containsAny" in data:
        import aws_sdk_qbusiness.types.document_attribute

        out["contains_any"] = (
            aws_sdk_qbusiness.types.document_attribute.deserialize_json(
                data["containsAny"]
            )
        )
    if "greaterThan" in data:
        import aws_sdk_qbusiness.types.document_attribute

        out["greater_than"] = (
            aws_sdk_qbusiness.types.document_attribute.deserialize_json(
                data["greaterThan"]
            )
        )
    if "greaterThanOrEquals" in data:
        import aws_sdk_qbusiness.types.document_attribute

        out["greater_than_or_equals"] = (
            aws_sdk_qbusiness.types.document_attribute.deserialize_json(
                data["greaterThanOrEquals"]
            )
        )
    if "lessThan" in data:
        import aws_sdk_qbusiness.types.document_attribute

        out["less_than"] = aws_sdk_qbusiness.types.document_attribute.deserialize_json(
            data["lessThan"]
        )
    if "lessThanOrEquals" in data:
        import aws_sdk_qbusiness.types.document_attribute

        out["less_than_or_equals"] = (
            aws_sdk_qbusiness.types.document_attribute.deserialize_json(
                data["lessThanOrEquals"]
            )
        )
    return out
