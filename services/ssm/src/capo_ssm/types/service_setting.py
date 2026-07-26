"""Generated from Smithy shape ``com.amazonaws.ssm#ServiceSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.date_time
    import capo_ssm.types.service_setting_id
    import capo_ssm.types.service_setting_value
    import capo_ssm.types.string


class ServiceSetting(TypedDict, closed=True):
    setting_id: NotRequired["capo_ssm.types.service_setting_id.ServiceSettingId"]
    """<p>The ID of the service setting.</p>"""
    setting_value: NotRequired[
        "capo_ssm.types.service_setting_value.ServiceSettingValue"
    ]
    """<p>The value of the service setting.</p>"""
    last_modified_date: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The last time the service setting was modified.</p>"""
    last_modified_user: NotRequired["capo_ssm.types.string.String"]
    """<p>The ARN of the last modified user. This field is populated only if the setting value was overwritten.</p>"""
    arn: NotRequired["capo_ssm.types.string.String"]
    """<p>The ARN of the service setting.</p>"""
    status: NotRequired["capo_ssm.types.string.String"]
    """<p>The status of the service setting. The value can be Default, Customized or PendingUpdate.</p> <ul> <li> <p>Default: The current setting uses a default value provisioned by the Amazon Web Services service team.</p> </li> <li> <p>Customized: The current setting use a custom value specified by the customer.</p> </li> <li> <p>PendingUpdate: The current setting uses a default or custom value, but a setting change request is pending approval.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceSetting) -> dict:
    out: dict = {}
    if "setting_id" in value:
        out["SettingId"] = value["setting_id"]
    if "setting_value" in value:
        out["SettingValue"] = value["setting_value"]
    if "last_modified_date" in value:
        import capo_ssm.types.date_time

        out["LastModifiedDate"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["last_modified_date"]
        )
    if "last_modified_user" in value:
        out["LastModifiedUser"] = value["last_modified_user"]
    if "arn" in value:
        out["ARN"] = value["arn"]
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceSetting:
    out: ServiceSetting = {}  # type: ignore[typeddict-item]
    if "SettingId" in data:
        out["setting_id"] = data["SettingId"]
    if "SettingValue" in data:
        out["setting_value"] = data["SettingValue"]
    if "LastModifiedDate" in data:
        import capo_ssm.types.date_time

        out["last_modified_date"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["LastModifiedDate"]
        )
    if "LastModifiedUser" in data:
        out["last_modified_user"] = data["LastModifiedUser"]
    if "ARN" in data:
        out["arn"] = data["ARN"]
    if "Status" in data:
        out["status"] = data["Status"]
    return out
