"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CredentialLockerSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.credential_locker_arn
    import capo_iot_managed_integrations.types.credential_locker_created_at
    import capo_iot_managed_integrations.types.credential_locker_id
    import capo_iot_managed_integrations.types.credential_locker_name


class CredentialLockerSummary(TypedDict, closed=True):
    id: NotRequired[
        "capo_iot_managed_integrations.types.credential_locker_id.CredentialLockerId"
    ]
    """<p>The id of the credential locker.</p>"""
    arn: NotRequired[
        "capo_iot_managed_integrations.types.credential_locker_arn.CredentialLockerArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the credential locker.</p>"""
    name: NotRequired[
        "capo_iot_managed_integrations.types.credential_locker_name.CredentialLockerName"
    ]
    """<p>The name of the credential locker.</p>"""
    created_at: NotRequired[
        "capo_iot_managed_integrations.types.credential_locker_created_at.CredentialLockerCreatedAt"
    ]
    """<p>The timestampe value of when the credential locker was created at.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CredentialLockerSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "created_at" in value:
        import capo_iot_managed_integrations.types.credential_locker_created_at

        out["CreatedAt"] = (
            capo_iot_managed_integrations.types.credential_locker_created_at.serialize_json(
                value["created_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> CredentialLockerSummary:
    out: CredentialLockerSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "CreatedAt" in data:
        import capo_iot_managed_integrations.types.credential_locker_created_at

        out["created_at"] = (
            capo_iot_managed_integrations.types.credential_locker_created_at.deserialize_json(
                data["CreatedAt"]
            )
        )
    return out
