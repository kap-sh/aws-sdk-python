"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#AppInstance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.chime_arn
    import capo_chime_sdk_identity.types.metadata
    import capo_chime_sdk_identity.types.non_empty_resource_name
    import capo_chime_sdk_identity.types.timestamp


class AppInstance(TypedDict, closed=True):
    app_instance_arn: NotRequired["capo_chime_sdk_identity.types.chime_arn.ChimeArn"]
    """<p>The ARN of the messaging instance.</p>"""
    name: NotRequired[
        "capo_chime_sdk_identity.types.non_empty_resource_name.NonEmptyResourceName"
    ]
    """<p>The name of an <code>AppInstance</code>.</p>"""
    created_timestamp: NotRequired["capo_chime_sdk_identity.types.timestamp.Timestamp"]
    """<p>The time at which an <code>AppInstance</code> was created. In epoch milliseconds.</p>"""
    last_updated_timestamp: NotRequired[
        "capo_chime_sdk_identity.types.timestamp.Timestamp"
    ]
    """<p>The time an <code>AppInstance</code> was last updated. In epoch milliseconds.</p>"""
    metadata: NotRequired["capo_chime_sdk_identity.types.metadata.Metadata"]
    """<p>The metadata of an <code>AppInstance</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppInstance) -> dict:
    out: dict = {}
    if "app_instance_arn" in value:
        out["AppInstanceArn"] = value["app_instance_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "created_timestamp" in value:
        import capo_chime_sdk_identity.types.timestamp

        out["CreatedTimestamp"] = (
            capo_chime_sdk_identity.types.timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    if "last_updated_timestamp" in value:
        import capo_chime_sdk_identity.types.timestamp

        out["LastUpdatedTimestamp"] = (
            capo_chime_sdk_identity.types.timestamp.serialize_json(
                value["last_updated_timestamp"]
            )
        )
    if "metadata" in value:
        out["Metadata"] = value["metadata"]
    return out


def deserialize_json(data: dict) -> AppInstance:
    out: AppInstance = {}  # type: ignore[typeddict-item]
    if "AppInstanceArn" in data:
        out["app_instance_arn"] = data["AppInstanceArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "CreatedTimestamp" in data:
        import capo_chime_sdk_identity.types.timestamp

        out["created_timestamp"] = (
            capo_chime_sdk_identity.types.timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if "LastUpdatedTimestamp" in data:
        import capo_chime_sdk_identity.types.timestamp

        out["last_updated_timestamp"] = (
            capo_chime_sdk_identity.types.timestamp.deserialize_json(
                data["LastUpdatedTimestamp"]
            )
        )
    if "Metadata" in data:
        out["metadata"] = data["Metadata"]
    return out
