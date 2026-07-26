"""Generated from Smithy shape ``com.amazonaws.qbusiness#ActionReview``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.action_payload_field_name_separator
    import capo_qbusiness.types.action_review_payload
    import capo_qbusiness.types.plugin_id
    import capo_qbusiness.types.plugin_type


class ActionReview(TypedDict, closed=True):
    plugin_id: NotRequired["capo_qbusiness.types.plugin_id.PluginId"]
    """<p>The identifier of the plugin associated with the action review.</p>"""
    plugin_type: NotRequired["capo_qbusiness.types.plugin_type.PluginType"]
    """<p>The type of plugin.</p>"""
    payload: NotRequired[
        "capo_qbusiness.types.action_review_payload.ActionReviewPayload"
    ]
    """<p>Field values that an end user needs to provide to Amazon Q Business for Amazon Q Business to perform the requested plugin action.</p>"""
    payload_field_name_separator: NotRequired[
        "capo_qbusiness.types.action_payload_field_name_separator.ActionPayloadFieldNameSeparator"
    ]
    """<p>A string used to retain information about the hierarchical contexts within an action review payload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionReview) -> dict:
    out: dict = {}
    if "plugin_id" in value:
        out["pluginId"] = value["plugin_id"]
    if "plugin_type" in value:
        import capo_qbusiness.types.plugin_type

        out["pluginType"] = capo_qbusiness.types.plugin_type.serialize_json(
            value["plugin_type"]
        )
    if "payload" in value:
        import capo_qbusiness.types.action_review_payload

        out["payload"] = capo_qbusiness.types.action_review_payload.serialize_json(
            value["payload"]
        )
    if "payload_field_name_separator" in value:
        out["payloadFieldNameSeparator"] = value["payload_field_name_separator"]
    return out


def deserialize_json(data: dict) -> ActionReview:
    out: ActionReview = {}  # type: ignore[typeddict-item]
    if "pluginId" in data:
        out["plugin_id"] = data["pluginId"]
    if "pluginType" in data:
        import capo_qbusiness.types.plugin_type

        out["plugin_type"] = capo_qbusiness.types.plugin_type.deserialize_json(
            data["pluginType"]
        )
    if "payload" in data:
        import capo_qbusiness.types.action_review_payload

        out["payload"] = capo_qbusiness.types.action_review_payload.deserialize_json(
            data["payload"]
        )
    if "payloadFieldNameSeparator" in data:
        out["payload_field_name_separator"] = data["payloadFieldNameSeparator"]
    return out
