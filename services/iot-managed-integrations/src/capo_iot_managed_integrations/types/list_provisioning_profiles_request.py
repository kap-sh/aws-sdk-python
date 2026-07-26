"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ListProvisioningProfilesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.max_results
    import capo_iot_managed_integrations.types.next_token


class ListProvisioningProfilesRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_iot_managed_integrations.types.next_token.NextToken"]
    """<p>A token that can be used to retrieve the next set of results.</p>"""
    max_results: NotRequired[
        "capo_iot_managed_integrations.types.max_results.MaxResults"
    ]
    """<p>The maximum number of results to return at one time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProvisioningProfilesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListProvisioningProfilesRequest:
    out: ListProvisioningProfilesRequest = {}  # type: ignore[typeddict-item]
    return out
