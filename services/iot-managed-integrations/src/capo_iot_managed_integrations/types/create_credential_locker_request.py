"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CreateCredentialLockerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.client_token
    import capo_iot_managed_integrations.types.credential_locker_name
    import capo_iot_managed_integrations.types.tags_map


class CreateCredentialLockerRequest(TypedDict, closed=True):
    name: NotRequired[
        "capo_iot_managed_integrations.types.credential_locker_name.CredentialLockerName"
    ]
    """<p>The name of the credential locker.</p>"""
    client_token: NotRequired[
        "capo_iot_managed_integrations.types.client_token.ClientToken"
    ]
    """<p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>"""
    tags: NotRequired["capo_iot_managed_integrations.types.tags_map.TagsMap"]
    """<p>A set of key/value pairs that are used to manage the credential locker.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCredentialLockerRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import capo_iot_managed_integrations.types.tags_map

        out["Tags"] = capo_iot_managed_integrations.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateCredentialLockerRequest:
    out: CreateCredentialLockerRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "Tags" in data:
        import capo_iot_managed_integrations.types.tags_map

        out["tags"] = capo_iot_managed_integrations.types.tags_map.deserialize_json(
            data["Tags"]
        )
    return out
