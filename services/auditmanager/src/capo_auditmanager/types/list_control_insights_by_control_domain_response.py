"""Generated from Smithy shape ``com.amazonaws.auditmanager#ListControlInsightsByControlDomainResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.control_insights_metadata
    import capo_auditmanager.types.token


class ListControlInsightsByControlDomainResponse(TypedDict, closed=True):
    control_insights_metadata: NotRequired[
        "capo_auditmanager.types.control_insights_metadata.ControlInsightsMetadata"
    ]
    """<p>The control analytics data that the <code>ListControlInsightsByControlDomain</code> API returned. </p>"""
    next_token: NotRequired["capo_auditmanager.types.token.Token"]
    """<p>The pagination token that's used to fetch the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListControlInsightsByControlDomainResponse) -> dict:
    out: dict = {}
    if "control_insights_metadata" in value:
        import capo_auditmanager.types.control_insights_metadata

        out["controlInsightsMetadata"] = (
            capo_auditmanager.types.control_insights_metadata.serialize_json(
                value["control_insights_metadata"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListControlInsightsByControlDomainResponse:
    out: ListControlInsightsByControlDomainResponse = {}  # type: ignore[typeddict-item]
    if "controlInsightsMetadata" in data:
        import capo_auditmanager.types.control_insights_metadata

        out["control_insights_metadata"] = (
            capo_auditmanager.types.control_insights_metadata.deserialize_json(
                data["controlInsightsMetadata"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
