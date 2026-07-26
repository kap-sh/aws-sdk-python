"""Generated from Smithy shape ``com.amazonaws.macie2#UsageStatisticsFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__list_of__string
    import capo_macie2.types.usage_statistics_filter_comparator
    import capo_macie2.types.usage_statistics_filter_key


class UsageStatisticsFilter(TypedDict, closed=True):
    comparator: NotRequired[
        "capo_macie2.types.usage_statistics_filter_comparator.UsageStatisticsFilterComparator"
    ]
    """<p>The operator to use in the condition. If the value for the key property is accountId, this value must be CONTAINS. If the value for the key property is any other supported field, this value can be EQ, GT, GTE, LT, LTE, or NE.</p>"""
    key: NotRequired[
        "capo_macie2.types.usage_statistics_filter_key.UsageStatisticsFilterKey"
    ]
    """<p>The field to use in the condition.</p>"""
    values: NotRequired["capo_macie2.types.__list_of__string.__listOf__string"]
    """<p>An array that lists values to use in the condition, based on the value for the field specified by the key property. If the value for the key property is accountId, this array can specify multiple values. Otherwise, this array can specify only one value.</p> <p>Valid values for each supported field are:</p> <ul><li><p>accountId - The unique identifier for an Amazon Web Services account.</p></li> <li><p>freeTrialStartDate - The date and time, in UTC and extended ISO 8601 format, when the Amazon Macie free trial started for an account.</p></li> <li><p>serviceLimit - A Boolean (true or false) value that indicates whether an account has reached its monthly quota.</p></li> <li><p>total - A string that represents the current estimated cost for an account.</p></li></ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: UsageStatisticsFilter) -> dict:
    out: dict = {}
    if "comparator" in value:
        import capo_macie2.types.usage_statistics_filter_comparator

        out["comparator"] = (
            capo_macie2.types.usage_statistics_filter_comparator.serialize_json(
                value["comparator"]
            )
        )
    if "key" in value:
        import capo_macie2.types.usage_statistics_filter_key

        out["key"] = capo_macie2.types.usage_statistics_filter_key.serialize_json(
            value["key"]
        )
    if "values" in value:
        import capo_macie2.types.__list_of__string

        out["values"] = capo_macie2.types.__list_of__string.serialize_json(
            value["values"]
        )
    return out


def deserialize_json(data: dict) -> UsageStatisticsFilter:
    out: UsageStatisticsFilter = {}  # type: ignore[typeddict-item]
    if "comparator" in data:
        import capo_macie2.types.usage_statistics_filter_comparator

        out["comparator"] = (
            capo_macie2.types.usage_statistics_filter_comparator.deserialize_json(
                data["comparator"]
            )
        )
    if "key" in data:
        import capo_macie2.types.usage_statistics_filter_key

        out["key"] = capo_macie2.types.usage_statistics_filter_key.deserialize_json(
            data["key"]
        )
    if "values" in data:
        import capo_macie2.types.__list_of__string

        out["values"] = capo_macie2.types.__list_of__string.deserialize_json(
            data["values"]
        )
    return out
