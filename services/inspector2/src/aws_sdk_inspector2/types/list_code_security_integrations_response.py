"""Generated from Smithy shape ``com.amazonaws.inspector2#ListCodeSecurityIntegrationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.integration_summaries


class ListCodeSecurityIntegrationsResponse(TypedDict):
    integrations: NotRequired[
        "aws_sdk_inspector2.types.integration_summaries.IntegrationSummaries"
    ]
    """<p>A list of code security integration summaries.</p>"""
    next_token: NotRequired["str"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the NextToken value returned from the previous request to continue listing results after the first page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCodeSecurityIntegrationsResponse) -> dict:
    out: dict = {}
    if "integrations" in value:
        import aws_sdk_inspector2.types.integration_summaries

        out["integrations"] = (
            aws_sdk_inspector2.types.integration_summaries.serialize_json(
                value["integrations"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCodeSecurityIntegrationsResponse:
    out: ListCodeSecurityIntegrationsResponse = {}  # type: ignore[typeddict-item]
    if "integrations" in data:
        import aws_sdk_inspector2.types.integration_summaries

        out["integrations"] = (
            aws_sdk_inspector2.types.integration_summaries.deserialize_json(
                data["integrations"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
