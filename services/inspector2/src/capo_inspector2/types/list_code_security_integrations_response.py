"""Generated from Smithy shape ``com.amazonaws.inspector2#ListCodeSecurityIntegrationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.integration_summaries


class ListCodeSecurityIntegrationsResponse(TypedDict, closed=True):
    integrations: NotRequired[
        "capo_inspector2.types.integration_summaries.IntegrationSummaries"
    ]
    """<p>A list of code security integration summaries.</p>"""
    next_token: NotRequired["str"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the NextToken value returned from the previous request to continue listing results after the first page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCodeSecurityIntegrationsResponse) -> dict:
    out: dict = {}
    if "integrations" in value:
        import capo_inspector2.types.integration_summaries

        out["integrations"] = (
            capo_inspector2.types.integration_summaries.serialize_json(
                value["integrations"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCodeSecurityIntegrationsResponse:
    out: ListCodeSecurityIntegrationsResponse = {}  # type: ignore[typeddict-item]
    if "integrations" in data:
        import capo_inspector2.types.integration_summaries

        out["integrations"] = (
            capo_inspector2.types.integration_summaries.deserialize_json(
                data["integrations"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
