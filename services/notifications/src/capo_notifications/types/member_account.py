"""Generated from Smithy shape ``com.amazonaws.notifications#MemberAccount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import capo_notifications.types.account_id
    import capo_notifications.types.member_account_notification_configuration_status
    import capo_notifications.types.notification_configuration_arn
    import capo_notifications.types.organizational_unit_id


class MemberAccount(TypedDict, closed=True):
    notification_configuration_arn: NotRequired[
        "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the notification configuration associated with the member account.</p>"""
    account_id: "capo_notifications.types.account_id.AccountId"
    """<p>The AWS account ID of the member account.</p>"""
    status: "capo_notifications.types.member_account_notification_configuration_status.MemberAccountNotificationConfigurationStatus"
    """<p>The current status of the member account.</p>"""
    status_reason: "str"
    """<p>The reason for the current status of the member account.</p>"""
    organizational_unit_id: (
        "capo_notifications.types.organizational_unit_id.OrganizationalUnitId"
    )
    """<p>The unique identifier of the organizational unit containing the member account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemberAccount) -> dict:
    out: dict = {}
    if "notification_configuration_arn" in value:
        out["notificationConfigurationArn"] = value["notification_configuration_arn"]
    out["accountId"] = value["account_id"]
    out["status"] = value["status"]
    out["statusReason"] = value["status_reason"]
    out["organizationalUnitId"] = value["organizational_unit_id"]
    return out


def deserialize_json(data: dict) -> MemberAccount:
    out: MemberAccount = {}  # type: ignore[typeddict-item]
    if "notificationConfigurationArn" in data:
        out["notification_configuration_arn"] = data["notificationConfigurationArn"]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError("MemberAccount.account_id required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("MemberAccount.status required")
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    else:
        raise DeserializationError("MemberAccount.status_reason required")
    if "organizationalUnitId" in data:
        out["organizational_unit_id"] = data["organizationalUnitId"]
    else:
        raise DeserializationError("MemberAccount.organizational_unit_id required")
    return out
