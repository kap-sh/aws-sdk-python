"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ListAccountAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.account_association_list_definition
    import capo_iot_managed_integrations.types.next_token


class ListAccountAssociationsResponse(TypedDict, closed=True):
    items: NotRequired[
        "capo_iot_managed_integrations.types.account_association_list_definition.AccountAssociationListDefinition"
    ]
    """<p>The list of account associations that match the specified criteria.</p>"""
    next_token: NotRequired["capo_iot_managed_integrations.types.next_token.NextToken"]
    """<p>A token used for pagination of results when there are more account associations than can be returned in a single response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccountAssociationsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_iot_managed_integrations.types.account_association_list_definition

        out["Items"] = (
            capo_iot_managed_integrations.types.account_association_list_definition.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAccountAssociationsResponse:
    out: ListAccountAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import capo_iot_managed_integrations.types.account_association_list_definition

        out["items"] = (
            capo_iot_managed_integrations.types.account_association_list_definition.deserialize_json(
                data["Items"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
