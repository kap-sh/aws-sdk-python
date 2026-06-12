"""Generated from Smithy shape ``com.amazonaws.connect#NotificationRecipientType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.user_id_list
    import aws_sdk_connect.types.user_tag_map


class NotificationRecipientType(TypedDict):
    user_tags: NotRequired["aws_sdk_connect.types.user_tag_map.UserTagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { \"Tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }. Connect Customer users with the specified tags will be notified.</p>"""
    user_ids: NotRequired["aws_sdk_connect.types.user_id_list.UserIdList"]
    """<p>A list of user IDs. Supports variable injection of <code>$.ContactLens.ContactEvaluation.Agent.AgentId</code> for <code>OnContactEvaluationSubmit</code> event source. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationRecipientType) -> dict:
    out: dict = {}
    if "user_tags" in value:
        import aws_sdk_connect.types.user_tag_map

        out["UserTags"] = aws_sdk_connect.types.user_tag_map.serialize_json(
            value["user_tags"]
        )
    if "user_ids" in value:
        import aws_sdk_connect.types.user_id_list

        out["UserIds"] = aws_sdk_connect.types.user_id_list.serialize_json(
            value["user_ids"]
        )
    return out


def deserialize_json(data: dict) -> NotificationRecipientType:
    out: NotificationRecipientType = {}  # type: ignore[typeddict-item]
    if "UserTags" in data:
        import aws_sdk_connect.types.user_tag_map

        out["user_tags"] = aws_sdk_connect.types.user_tag_map.deserialize_json(
            data["UserTags"]
        )
    if "UserIds" in data:
        import aws_sdk_connect.types.user_id_list

        out["user_ids"] = aws_sdk_connect.types.user_id_list.deserialize_json(
            data["UserIds"]
        )
    return out
