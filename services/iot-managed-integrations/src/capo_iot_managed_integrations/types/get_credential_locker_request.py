"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetCredentialLockerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.credential_locker_id


class GetCredentialLockerRequest(TypedDict, closed=True):
    identifier: (
        "capo_iot_managed_integrations.types.credential_locker_id.CredentialLockerId"
    )
    """<p>The identifier of the credential locker.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCredentialLockerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCredentialLockerRequest:
    out: GetCredentialLockerRequest = {}  # type: ignore[typeddict-item]
    return out
