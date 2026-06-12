"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CredentialLockerSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.credential_locker_arn
    import aws_sdk_iot_managed_integrations.types.credential_locker_created_at
    import aws_sdk_iot_managed_integrations.types.credential_locker_id
    import aws_sdk_iot_managed_integrations.types.credential_locker_name


class CredentialLockerSummary(TypedDict):
    id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.credential_locker_id.CredentialLockerId"
    ]
    """<p>The id of the credential locker.</p>"""
    arn: NotRequired[
        "aws_sdk_iot_managed_integrations.types.credential_locker_arn.CredentialLockerArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the credential locker.</p>"""
    name: NotRequired[
        "aws_sdk_iot_managed_integrations.types.credential_locker_name.CredentialLockerName"
    ]
    """<p>The name of the credential locker.</p>"""
    created_at: NotRequired[
        "aws_sdk_iot_managed_integrations.types.credential_locker_created_at.CredentialLockerCreatedAt"
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
        import aws_sdk_iot_managed_integrations.types.credential_locker_created_at

        out["CreatedAt"] = (
            aws_sdk_iot_managed_integrations.types.credential_locker_created_at.serialize_json(
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
        import aws_sdk_iot_managed_integrations.types.credential_locker_created_at

        out["created_at"] = (
            aws_sdk_iot_managed_integrations.types.credential_locker_created_at.deserialize_json(
                data["CreatedAt"]
            )
        )
    return out
