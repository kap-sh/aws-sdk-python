"""Generated from Smithy shape ``com.amazonaws.qconnect#QuickResponseSearchExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.quick_response_filter_field_list
    import capo_qconnect.types.quick_response_order_field
    import capo_qconnect.types.quick_response_query_field_list


class QuickResponseSearchExpression(TypedDict, closed=True):
    queries: NotRequired[
        "capo_qconnect.types.quick_response_query_field_list.QuickResponseQueryFieldList"
    ]
    """<p>The quick response query expressions.</p>"""
    filters: NotRequired[
        "capo_qconnect.types.quick_response_filter_field_list.QuickResponseFilterFieldList"
    ]
    """<p>The configuration of filtering rules applied to quick response query results.</p>"""
    order_on_field: NotRequired[
        "capo_qconnect.types.quick_response_order_field.QuickResponseOrderField"
    ]
    """<p>The quick response attribute fields on which the query results are ordered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuickResponseSearchExpression) -> dict:
    out: dict = {}
    if "queries" in value:
        import capo_qconnect.types.quick_response_query_field_list

        out["queries"] = (
            capo_qconnect.types.quick_response_query_field_list.serialize_json(
                value["queries"]
            )
        )
    if "filters" in value:
        import capo_qconnect.types.quick_response_filter_field_list

        out["filters"] = (
            capo_qconnect.types.quick_response_filter_field_list.serialize_json(
                value["filters"]
            )
        )
    if "order_on_field" in value:
        import capo_qconnect.types.quick_response_order_field

        out["orderOnField"] = (
            capo_qconnect.types.quick_response_order_field.serialize_json(
                value["order_on_field"]
            )
        )
    return out


def deserialize_json(data: dict) -> QuickResponseSearchExpression:
    out: QuickResponseSearchExpression = {}  # type: ignore[typeddict-item]
    if "queries" in data:
        import capo_qconnect.types.quick_response_query_field_list

        out["queries"] = (
            capo_qconnect.types.quick_response_query_field_list.deserialize_json(
                data["queries"]
            )
        )
    if "filters" in data:
        import capo_qconnect.types.quick_response_filter_field_list

        out["filters"] = (
            capo_qconnect.types.quick_response_filter_field_list.deserialize_json(
                data["filters"]
            )
        )
    if "orderOnField" in data:
        import capo_qconnect.types.quick_response_order_field

        out["order_on_field"] = (
            capo_qconnect.types.quick_response_order_field.deserialize_json(
                data["orderOnField"]
            )
        )
    return out
