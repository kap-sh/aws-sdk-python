"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DeleteCredentialLockerRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.credential_locker_id


class DeleteCredentialLockerRequest(TypedDict):
    identifier: (
        "aws_sdk_iot_managed_integrations.types.credential_locker_id.CredentialLockerId"
    )
    """<p>The identifier of the credential locker.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCredentialLockerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCredentialLockerRequest:
    out: DeleteCredentialLockerRequest = {}  # type: ignore[typeddict-item]
    return out
