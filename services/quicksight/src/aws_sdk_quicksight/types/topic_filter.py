"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.filter_class
    import aws_sdk_quicksight.types.limited_string
    import aws_sdk_quicksight.types.named_filter_type
    import aws_sdk_quicksight.types.synonyms
    import aws_sdk_quicksight.types.topic_category_filter
    import aws_sdk_quicksight.types.topic_date_range_filter
    import aws_sdk_quicksight.types.topic_null_filter
    import aws_sdk_quicksight.types.topic_numeric_equality_filter
    import aws_sdk_quicksight.types.topic_numeric_range_filter
    import aws_sdk_quicksight.types.topic_relative_date_filter


class TopicFilter(TypedDict, closed=True):
    filter_description: NotRequired[
        "aws_sdk_quicksight.types.limited_string.LimitedString"
    ]
    """<p>A description of the filter used to select items for a topic.</p>"""
    filter_class: NotRequired["aws_sdk_quicksight.types.filter_class.FilterClass"]
    """<p>The class of the filter. Valid values for this structure are <code>ENFORCED_VALUE_FILTER</code>, <code>CONDITIONAL_VALUE_FILTER</code>, and <code>NAMED_VALUE_FILTER</code>.</p>"""
    filter_name: "aws_sdk_quicksight.types.limited_string.LimitedString"
    """<p>The name of the filter.</p>"""
    filter_synonyms: NotRequired["aws_sdk_quicksight.types.synonyms.Synonyms"]
    """<p>The other names or aliases for the filter.</p>"""
    operand_field_name: "aws_sdk_quicksight.types.limited_string.LimitedString"
    """<p>The name of the field that the filter operates on.</p>"""
    filter_type: NotRequired[
        "aws_sdk_quicksight.types.named_filter_type.NamedFilterType"
    ]
    """<p>The type of the filter. Valid values for this structure are <code>CATEGORY_FILTER</code>, <code>NUMERIC_EQUALITY_FILTER</code>, <code>NUMERIC_RANGE_FILTER</code>, <code>DATE_RANGE_FILTER</code>, and <code>RELATIVE_DATE_FILTER</code>.</p>"""
    category_filter: NotRequired[
        "aws_sdk_quicksight.types.topic_category_filter.TopicCategoryFilter"
    ]
    """<p>The category filter that is associated with this filter.</p>"""
    numeric_equality_filter: NotRequired[
        "aws_sdk_quicksight.types.topic_numeric_equality_filter.TopicNumericEqualityFilter"
    ]
    """<p>The numeric equality filter.</p>"""
    numeric_range_filter: NotRequired[
        "aws_sdk_quicksight.types.topic_numeric_range_filter.TopicNumericRangeFilter"
    ]
    """<p>The numeric range filter.</p>"""
    date_range_filter: NotRequired[
        "aws_sdk_quicksight.types.topic_date_range_filter.TopicDateRangeFilter"
    ]
    """<p>The date range filter.</p>"""
    relative_date_filter: NotRequired[
        "aws_sdk_quicksight.types.topic_relative_date_filter.TopicRelativeDateFilter"
    ]
    """<p>The relative date filter.</p>"""
    null_filter: NotRequired[
        "aws_sdk_quicksight.types.topic_null_filter.TopicNullFilter"
    ]
    """<p>The null filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicFilter) -> dict:
    out: dict = {}
    if "filter_description" in value:
        out["FilterDescription"] = value["filter_description"]
    if "filter_class" in value:
        import aws_sdk_quicksight.types.filter_class

        out["FilterClass"] = aws_sdk_quicksight.types.filter_class.serialize_json(
            value["filter_class"]
        )
    out["FilterName"] = value["filter_name"]
    if "filter_synonyms" in value:
        import aws_sdk_quicksight.types.synonyms

        out["FilterSynonyms"] = aws_sdk_quicksight.types.synonyms.serialize_json(
            value["filter_synonyms"]
        )
    out["OperandFieldName"] = value["operand_field_name"]
    if "filter_type" in value:
        import aws_sdk_quicksight.types.named_filter_type

        out["FilterType"] = aws_sdk_quicksight.types.named_filter_type.serialize_json(
            value["filter_type"]
        )
    if "category_filter" in value:
        import aws_sdk_quicksight.types.topic_category_filter

        out["CategoryFilter"] = (
            aws_sdk_quicksight.types.topic_category_filter.serialize_json(
                value["category_filter"]
            )
        )
    if "numeric_equality_filter" in value:
        import aws_sdk_quicksight.types.topic_numeric_equality_filter

        out["NumericEqualityFilter"] = (
            aws_sdk_quicksight.types.topic_numeric_equality_filter.serialize_json(
                value["numeric_equality_filter"]
            )
        )
    if "numeric_range_filter" in value:
        import aws_sdk_quicksight.types.topic_numeric_range_filter

        out["NumericRangeFilter"] = (
            aws_sdk_quicksight.types.topic_numeric_range_filter.serialize_json(
                value["numeric_range_filter"]
            )
        )
    if "date_range_filter" in value:
        import aws_sdk_quicksight.types.topic_date_range_filter

        out["DateRangeFilter"] = (
            aws_sdk_quicksight.types.topic_date_range_filter.serialize_json(
                value["date_range_filter"]
            )
        )
    if "relative_date_filter" in value:
        import aws_sdk_quicksight.types.topic_relative_date_filter

        out["RelativeDateFilter"] = (
            aws_sdk_quicksight.types.topic_relative_date_filter.serialize_json(
                value["relative_date_filter"]
            )
        )
    if "null_filter" in value:
        import aws_sdk_quicksight.types.topic_null_filter

        out["NullFilter"] = aws_sdk_quicksight.types.topic_null_filter.serialize_json(
            value["null_filter"]
        )
    return out


def deserialize_json(data: dict) -> TopicFilter:
    out: TopicFilter = {}  # type: ignore[typeddict-item]
    if "FilterDescription" in data:
        out["filter_description"] = data["FilterDescription"]
    if "FilterClass" in data:
        import aws_sdk_quicksight.types.filter_class

        out["filter_class"] = aws_sdk_quicksight.types.filter_class.deserialize_json(
            data["FilterClass"]
        )
    if "FilterName" in data:
        out["filter_name"] = data["FilterName"]
    else:
        raise DeserializationError("TopicFilter.filter_name required")
    if "FilterSynonyms" in data:
        import aws_sdk_quicksight.types.synonyms

        out["filter_synonyms"] = aws_sdk_quicksight.types.synonyms.deserialize_json(
            data["FilterSynonyms"]
        )
    if "OperandFieldName" in data:
        out["operand_field_name"] = data["OperandFieldName"]
    else:
        raise DeserializationError("TopicFilter.operand_field_name required")
    if "FilterType" in data:
        import aws_sdk_quicksight.types.named_filter_type

        out["filter_type"] = (
            aws_sdk_quicksight.types.named_filter_type.deserialize_json(
                data["FilterType"]
            )
        )
    if "CategoryFilter" in data:
        import aws_sdk_quicksight.types.topic_category_filter

        out["category_filter"] = (
            aws_sdk_quicksight.types.topic_category_filter.deserialize_json(
                data["CategoryFilter"]
            )
        )
    if "NumericEqualityFilter" in data:
        import aws_sdk_quicksight.types.topic_numeric_equality_filter

        out["numeric_equality_filter"] = (
            aws_sdk_quicksight.types.topic_numeric_equality_filter.deserialize_json(
                data["NumericEqualityFilter"]
            )
        )
    if "NumericRangeFilter" in data:
        import aws_sdk_quicksight.types.topic_numeric_range_filter

        out["numeric_range_filter"] = (
            aws_sdk_quicksight.types.topic_numeric_range_filter.deserialize_json(
                data["NumericRangeFilter"]
            )
        )
    if "DateRangeFilter" in data:
        import aws_sdk_quicksight.types.topic_date_range_filter

        out["date_range_filter"] = (
            aws_sdk_quicksight.types.topic_date_range_filter.deserialize_json(
                data["DateRangeFilter"]
            )
        )
    if "RelativeDateFilter" in data:
        import aws_sdk_quicksight.types.topic_relative_date_filter

        out["relative_date_filter"] = (
            aws_sdk_quicksight.types.topic_relative_date_filter.deserialize_json(
                data["RelativeDateFilter"]
            )
        )
    if "NullFilter" in data:
        import aws_sdk_quicksight.types.topic_null_filter

        out["null_filter"] = (
            aws_sdk_quicksight.types.topic_null_filter.deserialize_json(
                data["NullFilter"]
            )
        )
    return out
