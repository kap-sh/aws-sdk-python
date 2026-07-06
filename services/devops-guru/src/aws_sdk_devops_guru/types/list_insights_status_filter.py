"""Generated from Smithy shape ``com.amazonaws.devopsguru#ListInsightsStatusFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.list_insights_any_status_filter
    import aws_sdk_devops_guru.types.list_insights_closed_status_filter
    import aws_sdk_devops_guru.types.list_insights_ongoing_status_filter


class ListInsightsStatusFilter(TypedDict, closed=True):
    ongoing: NotRequired[
        "aws_sdk_devops_guru.types.list_insights_ongoing_status_filter.ListInsightsOngoingStatusFilter"
    ]
    """<p> A <code>ListInsightsAnyStatusFilter</code> that specifies ongoing insights that are either <code>REACTIVE</code> or <code>PROACTIVE</code>. </p>"""
    closed: NotRequired[
        "aws_sdk_devops_guru.types.list_insights_closed_status_filter.ListInsightsClosedStatusFilter"
    ]
    """<p> A <code>ListInsightsClosedStatusFilter</code> that specifies closed insights that are either <code>REACTIVE</code> or <code>PROACTIVE</code>. </p>"""
    any: NotRequired[
        "aws_sdk_devops_guru.types.list_insights_any_status_filter.ListInsightsAnyStatusFilter"
    ]
    """<p> A <code>ListInsightsAnyStatusFilter</code> that specifies insights of any status that are either <code>REACTIVE</code> or <code>PROACTIVE</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInsightsStatusFilter) -> dict:
    out: dict = {}
    if "ongoing" in value:
        import aws_sdk_devops_guru.types.list_insights_ongoing_status_filter

        out["Ongoing"] = (
            aws_sdk_devops_guru.types.list_insights_ongoing_status_filter.serialize_json(
                value["ongoing"]
            )
        )
    if "closed" in value:
        import aws_sdk_devops_guru.types.list_insights_closed_status_filter

        out["Closed"] = (
            aws_sdk_devops_guru.types.list_insights_closed_status_filter.serialize_json(
                value["closed"]
            )
        )
    if "any" in value:
        import aws_sdk_devops_guru.types.list_insights_any_status_filter

        out["Any"] = (
            aws_sdk_devops_guru.types.list_insights_any_status_filter.serialize_json(
                value["any"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListInsightsStatusFilter:
    out: ListInsightsStatusFilter = {}  # type: ignore[typeddict-item]
    if "Ongoing" in data:
        import aws_sdk_devops_guru.types.list_insights_ongoing_status_filter

        out["ongoing"] = (
            aws_sdk_devops_guru.types.list_insights_ongoing_status_filter.deserialize_json(
                data["Ongoing"]
            )
        )
    if "Closed" in data:
        import aws_sdk_devops_guru.types.list_insights_closed_status_filter

        out["closed"] = (
            aws_sdk_devops_guru.types.list_insights_closed_status_filter.deserialize_json(
                data["Closed"]
            )
        )
    if "Any" in data:
        import aws_sdk_devops_guru.types.list_insights_any_status_filter

        out["any"] = (
            aws_sdk_devops_guru.types.list_insights_any_status_filter.deserialize_json(
                data["Any"]
            )
        )
    return out
