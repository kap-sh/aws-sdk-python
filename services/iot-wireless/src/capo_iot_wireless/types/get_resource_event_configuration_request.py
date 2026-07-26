"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetResourceEventConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.event_notification_partner_type
    import capo_iot_wireless.types.identifier
    import capo_iot_wireless.types.identifier_type


class GetResourceEventConfigurationRequest(TypedDict, closed=True):
    identifier: "capo_iot_wireless.types.identifier.Identifier"
    """<p>Resource identifier to opt in for event messaging.</p>"""
    identifier_type: "capo_iot_wireless.types.identifier_type.IdentifierType"
    """<p>Identifier type of the particular resource identifier for event configuration.</p>"""
    partner_type: NotRequired[
        "capo_iot_wireless.types.event_notification_partner_type.EventNotificationPartnerType"
    ]
    """<p>Partner type of the resource if the identifier type is <code>PartnerAccountId</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourceEventConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetResourceEventConfigurationRequest:
    out: GetResourceEventConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
