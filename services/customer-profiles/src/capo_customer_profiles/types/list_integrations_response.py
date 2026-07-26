"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListIntegrationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.integration_list
    import capo_customer_profiles.types.token


class ListIntegrationsResponse(TypedDict, closed=True):
    items: NotRequired["capo_customer_profiles.types.integration_list.IntegrationList"]
    """<p>The list of ListIntegrations instances.</p>"""
    next_token: NotRequired["capo_customer_profiles.types.token.token"]
    """<p>The pagination token from the previous ListIntegrations API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIntegrationsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_customer_profiles.types.integration_list

        out["Items"] = capo_customer_profiles.types.integration_list.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIntegrationsResponse:
    out: ListIntegrationsResponse = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import capo_customer_profiles.types.integration_list

        out["items"] = capo_customer_profiles.types.integration_list.deserialize_json(
            data["Items"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
