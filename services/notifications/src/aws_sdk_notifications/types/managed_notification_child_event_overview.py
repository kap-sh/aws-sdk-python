"""Generated from Smithy shape ``com.amazonaws.notifications#ManagedNotificationChildEventOverview``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_notifications.types.account_id
    import aws_sdk_notifications.types.creation_time
    import aws_sdk_notifications.types.managed_notification_child_event_summary
    import aws_sdk_notifications.types.managed_notification_configuration_os_arn
    import aws_sdk_notifications.types.managed_notification_event_arn
    import aws_sdk_notifications.types.organizational_unit_id


class ManagedNotificationChildEventOverview(TypedDict):
    arn: "aws_sdk_notifications.types.managed_notification_event_arn.ManagedNotificationEventArn"
    """<p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationChildEvent</code>.</p>"""
    managed_notification_configuration_arn: "aws_sdk_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn"
    """<p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationConfiguration</code>.</p>"""
    related_account: "aws_sdk_notifications.types.account_id.AccountId"
    """<p>The account that related to the <code>ManagedNotificationChildEvent</code>.</p>"""
    creation_time: "aws_sdk_notifications.types.creation_time.CreationTime"
    """<p>The creation time of the <code>ManagedNotificationChildEvent</code>.</p>"""
    child_event: "aws_sdk_notifications.types.managed_notification_child_event_summary.ManagedNotificationChildEventSummary"
    """<p>The content of the <code>ManagedNotificationChildEvent</code>.</p>"""
    aggregate_managed_notification_event_arn: "aws_sdk_notifications.types.managed_notification_event_arn.ManagedNotificationEventArn"
    """<p>The Amazon Resource Name (ARN) of the ManagedNotificationEvent that is associated with this <code>ManagedNotificationChildEvent</code>.</p>"""
    organizational_unit_id: NotRequired[
        "aws_sdk_notifications.types.organizational_unit_id.OrganizationalUnitId"
    ]
    """<p>The Organizational Unit Id that an AWS account belongs to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedNotificationChildEventOverview) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["managedNotificationConfigurationArn"] = value[
        "managed_notification_configuration_arn"
    ]
    out["relatedAccount"] = value["related_account"]
    import aws_sdk_notifications.types.creation_time

    out["creationTime"] = aws_sdk_notifications.types.creation_time.serialize_json(
        value["creation_time"]
    )
    import aws_sdk_notifications.types.managed_notification_child_event_summary

    out["childEvent"] = (
        aws_sdk_notifications.types.managed_notification_child_event_summary.serialize_json(
            value["child_event"]
        )
    )
    out["aggregateManagedNotificationEventArn"] = value[
        "aggregate_managed_notification_event_arn"
    ]
    if "organizational_unit_id" in value:
        out["organizationalUnitId"] = value["organizational_unit_id"]
    return out


def deserialize_json(data: dict) -> ManagedNotificationChildEventOverview:
    out: ManagedNotificationChildEventOverview = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ManagedNotificationChildEventOverview.arn required")
    if "managedNotificationConfigurationArn" in data:
        out["managed_notification_configuration_arn"] = data[
            "managedNotificationConfigurationArn"
        ]
    else:
        raise DeserializationError(
            "ManagedNotificationChildEventOverview.managed_notification_configuration_arn required"
        )
    if "relatedAccount" in data:
        out["related_account"] = data["relatedAccount"]
    else:
        raise DeserializationError(
            "ManagedNotificationChildEventOverview.related_account required"
        )
    if "creationTime" in data:
        import aws_sdk_notifications.types.creation_time

        out["creation_time"] = (
            aws_sdk_notifications.types.creation_time.deserialize_json(
                data["creationTime"]
            )
        )
    else:
        raise DeserializationError(
            "ManagedNotificationChildEventOverview.creation_time required"
        )
    if "childEvent" in data:
        import aws_sdk_notifications.types.managed_notification_child_event_summary

        out["child_event"] = (
            aws_sdk_notifications.types.managed_notification_child_event_summary.deserialize_json(
                data["childEvent"]
            )
        )
    else:
        raise DeserializationError(
            "ManagedNotificationChildEventOverview.child_event required"
        )
    if "aggregateManagedNotificationEventArn" in data:
        out["aggregate_managed_notification_event_arn"] = data[
            "aggregateManagedNotificationEventArn"
        ]
    else:
        raise DeserializationError(
            "ManagedNotificationChildEventOverview.aggregate_managed_notification_event_arn required"
        )
    if "organizationalUnitId" in data:
        out["organizational_unit_id"] = data["organizationalUnitId"]
    return out
