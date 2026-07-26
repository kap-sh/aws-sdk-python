"""Generated from Smithy shape ``com.amazonaws.kendra#FailedEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.entity_id
    import capo_kendra.types.error_message


class FailedEntity(TypedDict, closed=True):
    entity_id: NotRequired["capo_kendra.types.entity_id.EntityId"]
    """<p>The identifier of the user or group in your IAM Identity Center identity source. For example, a user ID could be an email.</p>"""
    error_message: NotRequired["capo_kendra.types.error_message.ErrorMessage"]
    """<p>The reason the user or group in your IAM Identity Center identity source failed to properly configure with your Amazon Kendra experience.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailedEntity) -> dict:
    out: dict = {}
    if "entity_id" in value:
        out["EntityId"] = value["entity_id"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FailedEntity:
    out: FailedEntity = {}  # type: ignore[typeddict-item]
    if "EntityId" in data:
        out["entity_id"] = data["EntityId"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
