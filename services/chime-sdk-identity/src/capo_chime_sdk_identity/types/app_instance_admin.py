"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#AppInstanceAdmin``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.chime_arn
    import capo_chime_sdk_identity.types.identity
    import capo_chime_sdk_identity.types.timestamp


class AppInstanceAdmin(TypedDict, closed=True):
    admin: NotRequired["capo_chime_sdk_identity.types.identity.Identity"]
    """<p>The <code>AppInstanceAdmin</code> data.</p>"""
    app_instance_arn: NotRequired["capo_chime_sdk_identity.types.chime_arn.ChimeArn"]
    """<p>The ARN of the <code>AppInstance</code> for which the user is an administrator.</p>"""
    created_timestamp: NotRequired["capo_chime_sdk_identity.types.timestamp.Timestamp"]
    """<p>The time at which an administrator was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppInstanceAdmin) -> dict:
    out: dict = {}
    if "admin" in value:
        import capo_chime_sdk_identity.types.identity

        out["Admin"] = capo_chime_sdk_identity.types.identity.serialize_json(
            value["admin"]
        )
    if "app_instance_arn" in value:
        out["AppInstanceArn"] = value["app_instance_arn"]
    if "created_timestamp" in value:
        import capo_chime_sdk_identity.types.timestamp

        out["CreatedTimestamp"] = (
            capo_chime_sdk_identity.types.timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    return out


def deserialize_json(data: dict) -> AppInstanceAdmin:
    out: AppInstanceAdmin = {}  # type: ignore[typeddict-item]
    if "Admin" in data:
        import capo_chime_sdk_identity.types.identity

        out["admin"] = capo_chime_sdk_identity.types.identity.deserialize_json(
            data["Admin"]
        )
    if "AppInstanceArn" in data:
        out["app_instance_arn"] = data["AppInstanceArn"]
    if "CreatedTimestamp" in data:
        import capo_chime_sdk_identity.types.timestamp

        out["created_timestamp"] = (
            capo_chime_sdk_identity.types.timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    return out
