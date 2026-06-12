"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#AppInstanceUser``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.chime_arn
    import aws_sdk_chime_sdk_identity.types.expiration_settings
    import aws_sdk_chime_sdk_identity.types.metadata
    import aws_sdk_chime_sdk_identity.types.timestamp
    import aws_sdk_chime_sdk_identity.types.user_name


class AppInstanceUser(TypedDict):
    app_instance_user_arn: NotRequired[
        "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn"
    ]
    """<p>The ARN of the <code>AppInstanceUser</code>.</p>"""
    name: NotRequired["aws_sdk_chime_sdk_identity.types.user_name.UserName"]
    """<p>The name of the <code>AppInstanceUser</code>.</p>"""
    metadata: NotRequired["aws_sdk_chime_sdk_identity.types.metadata.Metadata"]
    """<p>The metadata of the <code>AppInstanceUser</code>.</p>"""
    created_timestamp: NotRequired[
        "aws_sdk_chime_sdk_identity.types.timestamp.Timestamp"
    ]
    """<p>The time at which the <code>AppInstanceUser</code> was created.</p>"""
    last_updated_timestamp: NotRequired[
        "aws_sdk_chime_sdk_identity.types.timestamp.Timestamp"
    ]
    """<p>The time at which the <code>AppInstanceUser</code> was last updated.</p>"""
    expiration_settings: NotRequired[
        "aws_sdk_chime_sdk_identity.types.expiration_settings.ExpirationSettings"
    ]
    """<p>The interval after which an <code>AppInstanceUser</code> is automatically deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppInstanceUser) -> dict:
    out: dict = {}
    if "app_instance_user_arn" in value:
        out["AppInstanceUserArn"] = value["app_instance_user_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "metadata" in value:
        out["Metadata"] = value["metadata"]
    if "created_timestamp" in value:
        import aws_sdk_chime_sdk_identity.types.timestamp

        out["CreatedTimestamp"] = (
            aws_sdk_chime_sdk_identity.types.timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    if "last_updated_timestamp" in value:
        import aws_sdk_chime_sdk_identity.types.timestamp

        out["LastUpdatedTimestamp"] = (
            aws_sdk_chime_sdk_identity.types.timestamp.serialize_json(
                value["last_updated_timestamp"]
            )
        )
    if "expiration_settings" in value:
        import aws_sdk_chime_sdk_identity.types.expiration_settings

        out["ExpirationSettings"] = (
            aws_sdk_chime_sdk_identity.types.expiration_settings.serialize_json(
                value["expiration_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> AppInstanceUser:
    out: AppInstanceUser = {}  # type: ignore[typeddict-item]
    if "AppInstanceUserArn" in data:
        out["app_instance_user_arn"] = data["AppInstanceUserArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Metadata" in data:
        out["metadata"] = data["Metadata"]
    if "CreatedTimestamp" in data:
        import aws_sdk_chime_sdk_identity.types.timestamp

        out["created_timestamp"] = (
            aws_sdk_chime_sdk_identity.types.timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if "LastUpdatedTimestamp" in data:
        import aws_sdk_chime_sdk_identity.types.timestamp

        out["last_updated_timestamp"] = (
            aws_sdk_chime_sdk_identity.types.timestamp.deserialize_json(
                data["LastUpdatedTimestamp"]
            )
        )
    if "ExpirationSettings" in data:
        import aws_sdk_chime_sdk_identity.types.expiration_settings

        out["expiration_settings"] = (
            aws_sdk_chime_sdk_identity.types.expiration_settings.deserialize_json(
                data["ExpirationSettings"]
            )
        )
    return out
