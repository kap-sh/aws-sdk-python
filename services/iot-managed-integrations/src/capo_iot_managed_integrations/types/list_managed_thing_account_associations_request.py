"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ListManagedThingAccountAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.account_association_id
    import capo_iot_managed_integrations.types.managed_thing_id
    import capo_iot_managed_integrations.types.max_results
    import capo_iot_managed_integrations.types.next_token


class ListManagedThingAccountAssociationsRequest(TypedDict, closed=True):
    managed_thing_id: NotRequired[
        "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    ]
    """<p>The identifier of the managed thing to list account associations for.</p>"""
    account_association_id: NotRequired[
        "capo_iot_managed_integrations.types.account_association_id.AccountAssociationId"
    ]
    """<p>The identifier of the account association to filter results by. When specified, only associations with this account association ID will be returned.</p>"""
    max_results: NotRequired[
        "capo_iot_managed_integrations.types.max_results.MaxResults"
    ]
    """<p>The maximum number of account associations to return in a single response.</p>"""
    next_token: NotRequired["capo_iot_managed_integrations.types.next_token.NextToken"]
    """<p>A token used for pagination of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagedThingAccountAssociationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListManagedThingAccountAssociationsRequest:
    out: ListManagedThingAccountAssociationsRequest = {}  # type: ignore[typeddict-item]
    return out
