"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ListCredentialLockersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.credential_locker_list_definition
    import capo_iot_managed_integrations.types.next_token


class ListCredentialLockersResponse(TypedDict, closed=True):
    items: NotRequired[
        "capo_iot_managed_integrations.types.credential_locker_list_definition.CredentialLockerListDefinition"
    ]
    """<p>The list of credential lockers.</p>"""
    next_token: NotRequired["capo_iot_managed_integrations.types.next_token.NextToken"]
    """<p>A token that can be used to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCredentialLockersResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_iot_managed_integrations.types.credential_locker_list_definition

        out["Items"] = (
            capo_iot_managed_integrations.types.credential_locker_list_definition.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCredentialLockersResponse:
    out: ListCredentialLockersResponse = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import capo_iot_managed_integrations.types.credential_locker_list_definition

        out["items"] = (
            capo_iot_managed_integrations.types.credential_locker_list_definition.deserialize_json(
                data["Items"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
