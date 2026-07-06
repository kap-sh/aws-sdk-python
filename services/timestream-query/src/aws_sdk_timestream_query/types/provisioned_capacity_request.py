"""Generated from Smithy shape ``com.amazonaws.timestreamquery#ProvisionedCapacityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_timestream_query.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_query.types.account_settings_notification_configuration
    import aws_sdk_timestream_query.types.query_tcu


class ProvisionedCapacityRequest(TypedDict, closed=True):
    target_query_tcu: "aws_sdk_timestream_query.types.query_tcu.QueryTCU"
    """<p>The target compute capacity for querying data, specified in Timestream Compute Units (TCUs).</p>"""
    notification_configuration: NotRequired[
        "aws_sdk_timestream_query.types.account_settings_notification_configuration.AccountSettingsNotificationConfiguration"
    ]
    """<p>Configuration settings for notifications related to the provisioned capacity update.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProvisionedCapacityRequest) -> dict:
    out: dict = {}
    out["TargetQueryTCU"] = value["target_query_tcu"]
    if "notification_configuration" in value:
        import aws_sdk_timestream_query.types.account_settings_notification_configuration

        out["NotificationConfiguration"] = (
            aws_sdk_timestream_query.types.account_settings_notification_configuration.serialize_aws_json_1_0(
                value["notification_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ProvisionedCapacityRequest:
    out: ProvisionedCapacityRequest = {}  # type: ignore[typeddict-item]
    if "TargetQueryTCU" in data:
        out["target_query_tcu"] = data["TargetQueryTCU"]
    else:
        raise DeserializationError(
            "ProvisionedCapacityRequest.target_query_tcu required"
        )
    if "NotificationConfiguration" in data:
        import aws_sdk_timestream_query.types.account_settings_notification_configuration

        out["notification_configuration"] = (
            aws_sdk_timestream_query.types.account_settings_notification_configuration.deserialize_aws_json_1_0(
                data["NotificationConfiguration"]
            )
        )
    return out
