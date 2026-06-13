"""Generated from Smithy shape ``com.amazonaws.notifications#DisassociateOrganizationalUnitRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_notifications.types.notification_configuration_arn
    import aws_sdk_notifications.types.organizational_unit_id


class DisassociateOrganizationalUnitRequest(TypedDict):
    organizational_unit_id: (
        "aws_sdk_notifications.types.organizational_unit_id.OrganizationalUnitId"
    )
    """<p>The unique identifier of the organizational unit to disassociate.</p>"""
    notification_configuration_arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the notification configuration to disassociate from the organizational unit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateOrganizationalUnitRequest) -> dict:
    out: dict = {}
    out["notificationConfigurationArn"] = value["notification_configuration_arn"]
    return out


def deserialize_json(data: dict) -> DisassociateOrganizationalUnitRequest:
    out: DisassociateOrganizationalUnitRequest = {}  # type: ignore[typeddict-item]
    if "notificationConfigurationArn" in data:
        out["notification_configuration_arn"] = data["notificationConfigurationArn"]
    else:
        raise DeserializationError(
            "DisassociateOrganizationalUnitRequest.notification_configuration_arn required"
        )
    return out
