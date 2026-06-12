"""Generated from Smithy shape ``com.amazonaws.workmail#MobileDeviceAccessOverride``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workmail.types.device_id
    import aws_sdk_workmail.types.mobile_device_access_rule_description
    import aws_sdk_workmail.types.mobile_device_access_rule_effect
    import aws_sdk_workmail.types.timestamp
    import aws_sdk_workmail.types.work_mail_identifier


class MobileDeviceAccessOverride(TypedDict):
    user_id: NotRequired[
        "aws_sdk_workmail.types.work_mail_identifier.WorkMailIdentifier"
    ]
    """<p>The WorkMail user to which the access override applies.</p>"""
    device_id: NotRequired["aws_sdk_workmail.types.device_id.DeviceId"]
    """<p>The device to which the override applies.</p>"""
    effect: NotRequired[
        "aws_sdk_workmail.types.mobile_device_access_rule_effect.MobileDeviceAccessRuleEffect"
    ]
    """<p>The effect of the override, <code>ALLOW</code> or <code>DENY</code>.</p>"""
    description: NotRequired[
        "aws_sdk_workmail.types.mobile_device_access_rule_description.MobileDeviceAccessRuleDescription"
    ]
    """<p>A description of the override.</p>"""
    date_created: NotRequired["aws_sdk_workmail.types.timestamp.Timestamp"]
    """<p>The date the override was first created.</p>"""
    date_modified: NotRequired["aws_sdk_workmail.types.timestamp.Timestamp"]
    """<p>The date the override was last modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MobileDeviceAccessOverride) -> dict:
    out: dict = {}
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    if "device_id" in value:
        out["DeviceId"] = value["device_id"]
    if "effect" in value:
        import aws_sdk_workmail.types.mobile_device_access_rule_effect

        out["Effect"] = (
            aws_sdk_workmail.types.mobile_device_access_rule_effect.serialize_aws_json_1_1(
                value["effect"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "date_created" in value:
        import aws_sdk_workmail.types.timestamp

        out["DateCreated"] = aws_sdk_workmail.types.timestamp.serialize_aws_json_1_1(
            value["date_created"]
        )
    if "date_modified" in value:
        import aws_sdk_workmail.types.timestamp

        out["DateModified"] = aws_sdk_workmail.types.timestamp.serialize_aws_json_1_1(
            value["date_modified"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MobileDeviceAccessOverride:
    out: MobileDeviceAccessOverride = {}  # type: ignore[typeddict-item]
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    if "DeviceId" in data:
        out["device_id"] = data["DeviceId"]
    if "Effect" in data:
        import aws_sdk_workmail.types.mobile_device_access_rule_effect

        out["effect"] = (
            aws_sdk_workmail.types.mobile_device_access_rule_effect.deserialize_aws_json_1_1(
                data["Effect"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "DateCreated" in data:
        import aws_sdk_workmail.types.timestamp

        out["date_created"] = aws_sdk_workmail.types.timestamp.deserialize_aws_json_1_1(
            data["DateCreated"]
        )
    if "DateModified" in data:
        import aws_sdk_workmail.types.timestamp

        out["date_modified"] = (
            aws_sdk_workmail.types.timestamp.deserialize_aws_json_1_1(
                data["DateModified"]
            )
        )
    return out
