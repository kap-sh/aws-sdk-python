"""Generated from Smithy shape ``com.amazonaws.workmail#GetMobileDeviceAccessOverrideResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.device_id
    import capo_workmail.types.mobile_device_access_rule_description
    import capo_workmail.types.mobile_device_access_rule_effect
    import capo_workmail.types.timestamp
    import capo_workmail.types.work_mail_identifier


class GetMobileDeviceAccessOverrideResponse(TypedDict, closed=True):
    user_id: NotRequired["capo_workmail.types.work_mail_identifier.WorkMailIdentifier"]
    """<p>The WorkMail user to which the access override applies.</p>"""
    device_id: NotRequired["capo_workmail.types.device_id.DeviceId"]
    """<p>The device to which the access override applies.</p>"""
    effect: NotRequired[
        "capo_workmail.types.mobile_device_access_rule_effect.MobileDeviceAccessRuleEffect"
    ]
    """<p>The effect of the override, <code>ALLOW</code> or <code>DENY</code>.</p>"""
    description: NotRequired[
        "capo_workmail.types.mobile_device_access_rule_description.MobileDeviceAccessRuleDescription"
    ]
    """<p>A description of the override.</p>"""
    date_created: NotRequired["capo_workmail.types.timestamp.Timestamp"]
    """<p>The date the override was first created.</p>"""
    date_modified: NotRequired["capo_workmail.types.timestamp.Timestamp"]
    """<p>The date the description was last modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMobileDeviceAccessOverrideResponse) -> dict:
    out: dict = {}
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    if "device_id" in value:
        out["DeviceId"] = value["device_id"]
    if "effect" in value:
        import capo_workmail.types.mobile_device_access_rule_effect

        out["Effect"] = (
            capo_workmail.types.mobile_device_access_rule_effect.serialize_aws_json_1_1(
                value["effect"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "date_created" in value:
        import capo_workmail.types.timestamp

        out["DateCreated"] = capo_workmail.types.timestamp.serialize_aws_json_1_1(
            value["date_created"]
        )
    if "date_modified" in value:
        import capo_workmail.types.timestamp

        out["DateModified"] = capo_workmail.types.timestamp.serialize_aws_json_1_1(
            value["date_modified"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMobileDeviceAccessOverrideResponse:
    out: GetMobileDeviceAccessOverrideResponse = {}  # type: ignore[typeddict-item]
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    if "DeviceId" in data:
        out["device_id"] = data["DeviceId"]
    if "Effect" in data:
        import capo_workmail.types.mobile_device_access_rule_effect

        out["effect"] = (
            capo_workmail.types.mobile_device_access_rule_effect.deserialize_aws_json_1_1(
                data["Effect"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "DateCreated" in data:
        import capo_workmail.types.timestamp

        out["date_created"] = capo_workmail.types.timestamp.deserialize_aws_json_1_1(
            data["DateCreated"]
        )
    if "DateModified" in data:
        import capo_workmail.types.timestamp

        out["date_modified"] = capo_workmail.types.timestamp.deserialize_aws_json_1_1(
            data["DateModified"]
        )
    return out
