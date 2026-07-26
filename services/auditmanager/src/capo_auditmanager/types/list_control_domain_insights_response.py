"""Generated from Smithy shape ``com.amazonaws.auditmanager#ListControlDomainInsightsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.control_domain_insights_list
    import capo_auditmanager.types.token


class ListControlDomainInsightsResponse(TypedDict, closed=True):
    control_domain_insights: NotRequired[
        "capo_auditmanager.types.control_domain_insights_list.ControlDomainInsightsList"
    ]
    """<p>The control domain analytics data that the <code>ListControlDomainInsights</code> API returned. </p>"""
    next_token: NotRequired["capo_auditmanager.types.token.Token"]
    """<p>The pagination token that's used to fetch the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListControlDomainInsightsResponse) -> dict:
    out: dict = {}
    if "control_domain_insights" in value:
        import capo_auditmanager.types.control_domain_insights_list

        out["controlDomainInsights"] = (
            capo_auditmanager.types.control_domain_insights_list.serialize_json(
                value["control_domain_insights"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListControlDomainInsightsResponse:
    out: ListControlDomainInsightsResponse = {}  # type: ignore[typeddict-item]
    if "controlDomainInsights" in data:
        import capo_auditmanager.types.control_domain_insights_list

        out["control_domain_insights"] = (
            capo_auditmanager.types.control_domain_insights_list.deserialize_json(
                data["controlDomainInsights"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
