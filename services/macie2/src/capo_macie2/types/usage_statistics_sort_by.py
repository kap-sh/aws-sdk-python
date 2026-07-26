"""Generated from Smithy shape ``com.amazonaws.macie2#UsageStatisticsSortBy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.order_by
    import capo_macie2.types.usage_statistics_sort_key


class UsageStatisticsSortBy(TypedDict, closed=True):
    key: NotRequired[
        "capo_macie2.types.usage_statistics_sort_key.UsageStatisticsSortKey"
    ]
    """<p>The field to sort the results by.</p>"""
    order_by: NotRequired["capo_macie2.types.order_by.OrderBy"]
    """<p>The sort order to apply to the results, based on the value for the field specified by the key property. Valid values are: ASC, sort the results in ascending order; and, DESC, sort the results in descending order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UsageStatisticsSortBy) -> dict:
    out: dict = {}
    if "key" in value:
        import capo_macie2.types.usage_statistics_sort_key

        out["key"] = capo_macie2.types.usage_statistics_sort_key.serialize_json(
            value["key"]
        )
    if "order_by" in value:
        import capo_macie2.types.order_by

        out["orderBy"] = capo_macie2.types.order_by.serialize_json(value["order_by"])
    return out


def deserialize_json(data: dict) -> UsageStatisticsSortBy:
    out: UsageStatisticsSortBy = {}  # type: ignore[typeddict-item]
    if "key" in data:
        import capo_macie2.types.usage_statistics_sort_key

        out["key"] = capo_macie2.types.usage_statistics_sort_key.deserialize_json(
            data["key"]
        )
    if "orderBy" in data:
        import capo_macie2.types.order_by

        out["order_by"] = capo_macie2.types.order_by.deserialize_json(data["orderBy"])
    return out
