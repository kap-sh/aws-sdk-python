"""Generated from Smithy shape ``com.amazonaws.entityresolution#ListProviderServicesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.next_token
    import capo_entityresolution.types.provider_service_list


class ListProviderServicesOutput(TypedDict, closed=True):
    provider_service_summaries: NotRequired[
        "capo_entityresolution.types.provider_service_list.ProviderServiceList"
    ]
    """<p>A list of <code>ProviderServices</code> objects.</p>"""
    next_token: NotRequired["capo_entityresolution.types.next_token.NextToken"]
    """<p>The pagination token from the previous API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProviderServicesOutput) -> dict:
    out: dict = {}
    if "provider_service_summaries" in value:
        import capo_entityresolution.types.provider_service_list

        out["providerServiceSummaries"] = (
            capo_entityresolution.types.provider_service_list.serialize_json(
                value["provider_service_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListProviderServicesOutput:
    out: ListProviderServicesOutput = {}  # type: ignore[typeddict-item]
    if "providerServiceSummaries" in data:
        import capo_entityresolution.types.provider_service_list

        out["provider_service_summaries"] = (
            capo_entityresolution.types.provider_service_list.deserialize_json(
                data["providerServiceSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
