"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CreateCredentialLockerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.credential_locker_arn
    import aws_sdk_iot_managed_integrations.types.credential_locker_created_at
    import aws_sdk_iot_managed_integrations.types.credential_locker_id


class CreateCredentialLockerResponse(TypedDict, closed=True):
    id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.credential_locker_id.CredentialLockerId"
    ]
    """<p>The identifier of the credential locker creation request.</p>"""
    arn: NotRequired[
        "aws_sdk_iot_managed_integrations.types.credential_locker_arn.CredentialLockerArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the credential locker.</p>"""
    created_at: NotRequired[
        "aws_sdk_iot_managed_integrations.types.credential_locker_created_at.CredentialLockerCreatedAt"
    ]
    """<p>The timestamp value of when the credential locker request occurred.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCredentialLockerResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "created_at" in value:
        import aws_sdk_iot_managed_integrations.types.credential_locker_created_at

        out["CreatedAt"] = (
            aws_sdk_iot_managed_integrations.types.credential_locker_created_at.serialize_json(
                value["created_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateCredentialLockerResponse:
    out: CreateCredentialLockerResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "CreatedAt" in data:
        import aws_sdk_iot_managed_integrations.types.credential_locker_created_at

        out["created_at"] = (
            aws_sdk_iot_managed_integrations.types.credential_locker_created_at.deserialize_json(
                data["CreatedAt"]
            )
        )
    return out
