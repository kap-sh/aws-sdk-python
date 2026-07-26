"""Generated from Smithy shape ``com.amazonaws.timestreamquery#ProvisionedCapacityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_query.types.account_settings_notification_configuration
    import capo_timestream_query.types.last_update
    import capo_timestream_query.types.query_tcu


class ProvisionedCapacityResponse(TypedDict, closed=True):
    active_query_tcu: NotRequired["capo_timestream_query.types.query_tcu.QueryTCU"]
    """<p>The number of Timestream Compute Units (TCUs) provisioned in the account. This field is only visible when the compute mode is <code>PROVISIONED</code>.</p>"""
    notification_configuration: NotRequired[
        "capo_timestream_query.types.account_settings_notification_configuration.AccountSettingsNotificationConfiguration"
    ]
    """<p>An object that contains settings for notifications that are sent whenever the provisioned capacity settings are modified. This field is only visible when the compute mode is <code>PROVISIONED</code>.</p>"""
    last_update: NotRequired["capo_timestream_query.types.last_update.LastUpdate"]
    """<p>Information about the last update to the provisioned capacity settings.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProvisionedCapacityResponse) -> dict:
    out: dict = {}
    if "active_query_tcu" in value:
        out["ActiveQueryTCU"] = value["active_query_tcu"]
    if "notification_configuration" in value:
        import capo_timestream_query.types.account_settings_notification_configuration

        out["NotificationConfiguration"] = (
            capo_timestream_query.types.account_settings_notification_configuration.serialize_aws_json_1_0(
                value["notification_configuration"]
            )
        )
    if "last_update" in value:
        import capo_timestream_query.types.last_update

        out["LastUpdate"] = (
            capo_timestream_query.types.last_update.serialize_aws_json_1_0(
                value["last_update"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ProvisionedCapacityResponse:
    out: ProvisionedCapacityResponse = {}  # type: ignore[typeddict-item]
    if "ActiveQueryTCU" in data:
        out["active_query_tcu"] = data["ActiveQueryTCU"]
    if "NotificationConfiguration" in data:
        import capo_timestream_query.types.account_settings_notification_configuration

        out["notification_configuration"] = (
            capo_timestream_query.types.account_settings_notification_configuration.deserialize_aws_json_1_0(
                data["NotificationConfiguration"]
            )
        )
    if "LastUpdate" in data:
        import capo_timestream_query.types.last_update

        out["last_update"] = (
            capo_timestream_query.types.last_update.deserialize_aws_json_1_0(
                data["LastUpdate"]
            )
        )
    return out
