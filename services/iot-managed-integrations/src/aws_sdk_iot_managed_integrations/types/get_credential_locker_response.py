"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetCredentialLockerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.credential_locker_arn
    import aws_sdk_iot_managed_integrations.types.credential_locker_created_at
    import aws_sdk_iot_managed_integrations.types.credential_locker_id
    import aws_sdk_iot_managed_integrations.types.credential_locker_name
    import aws_sdk_iot_managed_integrations.types.tags_map


class GetCredentialLockerResponse(TypedDict, closed=True):
    id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.credential_locker_id.CredentialLockerId"
    ]
    """<p>The identifier of the credential locker.</p>"""
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
    """<p>The timestamp value of when the credential locker requset occurred.</p>"""
    tags: NotRequired["aws_sdk_iot_managed_integrations.types.tags_map.TagsMap"]
    """<p>A set of key/value pairs that are used to manage the credential locker.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCredentialLockerResponse) -> dict:
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
    if "tags" in value:
        import aws_sdk_iot_managed_integrations.types.tags_map

        out["Tags"] = aws_sdk_iot_managed_integrations.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> GetCredentialLockerResponse:
    out: GetCredentialLockerResponse = {}  # type: ignore[typeddict-item]
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
    if "Tags" in data:
        import aws_sdk_iot_managed_integrations.types.tags_map

        out["tags"] = aws_sdk_iot_managed_integrations.types.tags_map.deserialize_json(
            data["Tags"]
        )
    return out
