"""Generated from Smithy shape ``com.amazonaws.workmail#MobileDeviceAccessRule``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workmail.types.device_model_list
    import aws_sdk_workmail.types.device_operating_system_list
    import aws_sdk_workmail.types.device_type_list
    import aws_sdk_workmail.types.device_user_agent_list
    import aws_sdk_workmail.types.mobile_device_access_rule_description
    import aws_sdk_workmail.types.mobile_device_access_rule_effect
    import aws_sdk_workmail.types.mobile_device_access_rule_id
    import aws_sdk_workmail.types.mobile_device_access_rule_name
    import aws_sdk_workmail.types.timestamp


class MobileDeviceAccessRule(TypedDict):
    mobile_device_access_rule_id: NotRequired[
        "aws_sdk_workmail.types.mobile_device_access_rule_id.MobileDeviceAccessRuleId"
    ]
    """<p>The ID assigned to a mobile access rule.</p>"""
    name: NotRequired[
        "aws_sdk_workmail.types.mobile_device_access_rule_name.MobileDeviceAccessRuleName"
    ]
    """<p>The name of a mobile access rule.</p>"""
    description: NotRequired[
        "aws_sdk_workmail.types.mobile_device_access_rule_description.MobileDeviceAccessRuleDescription"
    ]
    """<p>The description of a mobile access rule.</p>"""
    effect: NotRequired[
        "aws_sdk_workmail.types.mobile_device_access_rule_effect.MobileDeviceAccessRuleEffect"
    ]
    """<p>The effect of the rule when it matches. Allowed values are <code>ALLOW</code> or <code>DENY</code>.</p>"""
    device_types: NotRequired["aws_sdk_workmail.types.device_type_list.DeviceTypeList"]
    """<p>Device types that a rule will match.</p>"""
    not_device_types: NotRequired[
        "aws_sdk_workmail.types.device_type_list.DeviceTypeList"
    ]
    """<p>Device types that a rule <b>will not</b> match. All other device types will match.</p>"""
    device_models: NotRequired[
        "aws_sdk_workmail.types.device_model_list.DeviceModelList"
    ]
    """<p>Device models that a rule will match.</p>"""
    not_device_models: NotRequired[
        "aws_sdk_workmail.types.device_model_list.DeviceModelList"
    ]
    """<p>Device models that a rule <b>will not</b> match. All other device models will match.</p>"""
    device_operating_systems: NotRequired[
        "aws_sdk_workmail.types.device_operating_system_list.DeviceOperatingSystemList"
    ]
    """<p>Device operating systems that a rule will match.</p>"""
    not_device_operating_systems: NotRequired[
        "aws_sdk_workmail.types.device_operating_system_list.DeviceOperatingSystemList"
    ]
    """<p>Device operating systems that a rule <b>will not</b> match. All other device types will match.</p>"""
    device_user_agents: NotRequired[
        "aws_sdk_workmail.types.device_user_agent_list.DeviceUserAgentList"
    ]
    """<p>Device user agents that a rule will match.</p>"""
    not_device_user_agents: NotRequired[
        "aws_sdk_workmail.types.device_user_agent_list.DeviceUserAgentList"
    ]
    """<p>Device user agents that a rule <b>will not</b> match. All other device user agents will match.</p>"""
    date_created: NotRequired["aws_sdk_workmail.types.timestamp.Timestamp"]
    """<p>The date and time at which an access rule was created.</p>"""
    date_modified: NotRequired["aws_sdk_workmail.types.timestamp.Timestamp"]
    """<p>The date and time at which an access rule was modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MobileDeviceAccessRule) -> dict:
    out: dict = {}
    if "mobile_device_access_rule_id" in value:
        out["MobileDeviceAccessRuleId"] = value["mobile_device_access_rule_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "effect" in value:
        import aws_sdk_workmail.types.mobile_device_access_rule_effect

        out["Effect"] = (
            aws_sdk_workmail.types.mobile_device_access_rule_effect.serialize_aws_json_1_1(
                value["effect"]
            )
        )
    if "device_types" in value:
        import aws_sdk_workmail.types.device_type_list

        out["DeviceTypes"] = (
            aws_sdk_workmail.types.device_type_list.serialize_aws_json_1_1(
                value["device_types"]
            )
        )
    if "not_device_types" in value:
        import aws_sdk_workmail.types.device_type_list

        out["NotDeviceTypes"] = (
            aws_sdk_workmail.types.device_type_list.serialize_aws_json_1_1(
                value["not_device_types"]
            )
        )
    if "device_models" in value:
        import aws_sdk_workmail.types.device_model_list

        out["DeviceModels"] = (
            aws_sdk_workmail.types.device_model_list.serialize_aws_json_1_1(
                value["device_models"]
            )
        )
    if "not_device_models" in value:
        import aws_sdk_workmail.types.device_model_list

        out["NotDeviceModels"] = (
            aws_sdk_workmail.types.device_model_list.serialize_aws_json_1_1(
                value["not_device_models"]
            )
        )
    if "device_operating_systems" in value:
        import aws_sdk_workmail.types.device_operating_system_list

        out["DeviceOperatingSystems"] = (
            aws_sdk_workmail.types.device_operating_system_list.serialize_aws_json_1_1(
                value["device_operating_systems"]
            )
        )
    if "not_device_operating_systems" in value:
        import aws_sdk_workmail.types.device_operating_system_list

        out["NotDeviceOperatingSystems"] = (
            aws_sdk_workmail.types.device_operating_system_list.serialize_aws_json_1_1(
                value["not_device_operating_systems"]
            )
        )
    if "device_user_agents" in value:
        import aws_sdk_workmail.types.device_user_agent_list

        out["DeviceUserAgents"] = (
            aws_sdk_workmail.types.device_user_agent_list.serialize_aws_json_1_1(
                value["device_user_agents"]
            )
        )
    if "not_device_user_agents" in value:
        import aws_sdk_workmail.types.device_user_agent_list

        out["NotDeviceUserAgents"] = (
            aws_sdk_workmail.types.device_user_agent_list.serialize_aws_json_1_1(
                value["not_device_user_agents"]
            )
        )
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


def deserialize_aws_json_1_1(data: dict) -> MobileDeviceAccessRule:
    out: MobileDeviceAccessRule = {}  # type: ignore[typeddict-item]
    if "MobileDeviceAccessRuleId" in data:
        out["mobile_device_access_rule_id"] = data["MobileDeviceAccessRuleId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Effect" in data:
        import aws_sdk_workmail.types.mobile_device_access_rule_effect

        out["effect"] = (
            aws_sdk_workmail.types.mobile_device_access_rule_effect.deserialize_aws_json_1_1(
                data["Effect"]
            )
        )
    if "DeviceTypes" in data:
        import aws_sdk_workmail.types.device_type_list

        out["device_types"] = (
            aws_sdk_workmail.types.device_type_list.deserialize_aws_json_1_1(
                data["DeviceTypes"]
            )
        )
    if "NotDeviceTypes" in data:
        import aws_sdk_workmail.types.device_type_list

        out["not_device_types"] = (
            aws_sdk_workmail.types.device_type_list.deserialize_aws_json_1_1(
                data["NotDeviceTypes"]
            )
        )
    if "DeviceModels" in data:
        import aws_sdk_workmail.types.device_model_list

        out["device_models"] = (
            aws_sdk_workmail.types.device_model_list.deserialize_aws_json_1_1(
                data["DeviceModels"]
            )
        )
    if "NotDeviceModels" in data:
        import aws_sdk_workmail.types.device_model_list

        out["not_device_models"] = (
            aws_sdk_workmail.types.device_model_list.deserialize_aws_json_1_1(
                data["NotDeviceModels"]
            )
        )
    if "DeviceOperatingSystems" in data:
        import aws_sdk_workmail.types.device_operating_system_list

        out["device_operating_systems"] = (
            aws_sdk_workmail.types.device_operating_system_list.deserialize_aws_json_1_1(
                data["DeviceOperatingSystems"]
            )
        )
    if "NotDeviceOperatingSystems" in data:
        import aws_sdk_workmail.types.device_operating_system_list

        out["not_device_operating_systems"] = (
            aws_sdk_workmail.types.device_operating_system_list.deserialize_aws_json_1_1(
                data["NotDeviceOperatingSystems"]
            )
        )
    if "DeviceUserAgents" in data:
        import aws_sdk_workmail.types.device_user_agent_list

        out["device_user_agents"] = (
            aws_sdk_workmail.types.device_user_agent_list.deserialize_aws_json_1_1(
                data["DeviceUserAgents"]
            )
        )
    if "NotDeviceUserAgents" in data:
        import aws_sdk_workmail.types.device_user_agent_list

        out["not_device_user_agents"] = (
            aws_sdk_workmail.types.device_user_agent_list.deserialize_aws_json_1_1(
                data["NotDeviceUserAgents"]
            )
        )
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
