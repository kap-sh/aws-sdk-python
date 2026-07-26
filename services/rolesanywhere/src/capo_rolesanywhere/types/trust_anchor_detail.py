"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#TrustAnchorDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_rolesanywhere.types.notification_setting_details
    import capo_rolesanywhere.types.resource_name
    import capo_rolesanywhere.types.source
    import capo_rolesanywhere.types.uuid


class TrustAnchorDetail(TypedDict, closed=True):
    trust_anchor_id: NotRequired["capo_rolesanywhere.types.uuid.Uuid"]
    """<p>The unique identifier of the trust anchor.</p>"""
    trust_anchor_arn: NotRequired["str"]
    """<p>The ARN of the trust anchor.</p>"""
    name: NotRequired["capo_rolesanywhere.types.resource_name.ResourceName"]
    """<p>The name of the trust anchor.</p>"""
    source: NotRequired["capo_rolesanywhere.types.source.Source"]
    """<p>The trust anchor type and its related certificate data.</p>"""
    enabled: NotRequired["bool"]
    """<p>Indicates whether the trust anchor is enabled.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The ISO-8601 timestamp when the trust anchor was created. </p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The ISO-8601 timestamp when the trust anchor was last updated. </p>"""
    notification_settings: NotRequired[
        "capo_rolesanywhere.types.notification_setting_details.NotificationSettingDetails"
    ]
    """<p>A list of notification settings to be associated to the trust anchor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrustAnchorDetail) -> dict:
    out: dict = {}
    if "trust_anchor_id" in value:
        out["trustAnchorId"] = value["trust_anchor_id"]
    if "trust_anchor_arn" in value:
        out["trustAnchorArn"] = value["trust_anchor_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "source" in value:
        import capo_rolesanywhere.types.source

        out["source"] = capo_rolesanywhere.types.source.serialize_json(value["source"])
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "created_at" in value:
        import capo_rolesanywhere.types._prelude.timestamp

        out["createdAt"] = capo_rolesanywhere.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_rolesanywhere.types._prelude.timestamp

        out["updatedAt"] = capo_rolesanywhere.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    if "notification_settings" in value:
        import capo_rolesanywhere.types.notification_setting_details

        out["notificationSettings"] = (
            capo_rolesanywhere.types.notification_setting_details.serialize_json(
                value["notification_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> TrustAnchorDetail:
    out: TrustAnchorDetail = {}  # type: ignore[typeddict-item]
    if "trustAnchorId" in data:
        out["trust_anchor_id"] = data["trustAnchorId"]
    if "trustAnchorArn" in data:
        out["trust_anchor_arn"] = data["trustAnchorArn"]
    if "name" in data:
        out["name"] = data["name"]
    if "source" in data:
        import capo_rolesanywhere.types.source

        out["source"] = capo_rolesanywhere.types.source.deserialize_json(data["source"])
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    if "createdAt" in data:
        import capo_rolesanywhere.types._prelude.timestamp

        out["created_at"] = (
            capo_rolesanywhere.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import capo_rolesanywhere.types._prelude.timestamp

        out["updated_at"] = (
            capo_rolesanywhere.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    if "notificationSettings" in data:
        import capo_rolesanywhere.types.notification_setting_details

        out["notification_settings"] = (
            capo_rolesanywhere.types.notification_setting_details.deserialize_json(
                data["notificationSettings"]
            )
        )
    return out
