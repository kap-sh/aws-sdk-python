"""Generated from Smithy shape ``com.amazonaws.workmail#MobileDeviceAccessRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.device_model_list
    import capo_workmail.types.device_operating_system_list
    import capo_workmail.types.device_type_list
    import capo_workmail.types.device_user_agent_list
    import capo_workmail.types.mobile_device_access_rule_description
    import capo_workmail.types.mobile_device_access_rule_effect
    import capo_workmail.types.mobile_device_access_rule_id
    import capo_workmail.types.mobile_device_access_rule_name
    import capo_workmail.types.timestamp


class MobileDeviceAccessRule(TypedDict, closed=True):
    mobile_device_access_rule_id: NotRequired[
        "capo_workmail.types.mobile_device_access_rule_id.MobileDeviceAccessRuleId"
    ]
    """<p>The ID assigned to a mobile access rule.</p>"""
    name: NotRequired[
        "capo_workmail.types.mobile_device_access_rule_name.MobileDeviceAccessRuleName"
    ]
    """<p>The name of a mobile access rule.</p>"""
    description: NotRequired[
        "capo_workmail.types.mobile_device_access_rule_description.MobileDeviceAccessRuleDescription"
    ]
    """<p>The description of a mobile access rule.</p>"""
    effect: NotRequired[
        "capo_workmail.types.mobile_device_access_rule_effect.MobileDeviceAccessRuleEffect"
    ]
    """<p>The effect of the rule when it matches. Allowed values are <code>ALLOW</code> or <code>DENY</code>.</p>"""
    device_types: NotRequired["capo_workmail.types.device_type_list.DeviceTypeList"]
    """<p>Device types that a rule will match.</p>"""
    not_device_types: NotRequired["capo_workmail.types.device_type_list.DeviceTypeList"]
    """<p>Device types that a rule <b>will not</b> match. All other device types will match.</p>"""
    device_models: NotRequired["capo_workmail.types.device_model_list.DeviceModelList"]
    """<p>Device models that a rule will match.</p>"""
    not_device_models: NotRequired[
        "capo_workmail.types.device_model_list.DeviceModelList"
    ]
    """<p>Device models that a rule <b>will not</b> match. All other device models will match.</p>"""
    device_operating_systems: NotRequired[
        "capo_workmail.types.device_operating_system_list.DeviceOperatingSystemList"
    ]
    """<p>Device operating systems that a rule will match.</p>"""
    not_device_operating_systems: NotRequired[
        "capo_workmail.types.device_operating_system_list.DeviceOperatingSystemList"
    ]
    """<p>Device operating systems that a rule <b>will not</b> match. All other device types will match.</p>"""
    device_user_agents: NotRequired[
        "capo_workmail.types.device_user_agent_list.DeviceUserAgentList"
    ]
    """<p>Device user agents that a rule will match.</p>"""
    not_device_user_agents: NotRequired[
        "capo_workmail.types.device_user_agent_list.DeviceUserAgentList"
    ]
    """<p>Device user agents that a rule <b>will not</b> match. All other device user agents will match.</p>"""
    date_created: NotRequired["capo_workmail.types.timestamp.Timestamp"]
    """<p>The date and time at which an access rule was created.</p>"""
    date_modified: NotRequired["capo_workmail.types.timestamp.Timestamp"]
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
        import capo_workmail.types.mobile_device_access_rule_effect

        out["Effect"] = (
            capo_workmail.types.mobile_device_access_rule_effect.serialize_aws_json_1_1(
                value["effect"]
            )
        )
    if "device_types" in value:
        import capo_workmail.types.device_type_list

        out["DeviceTypes"] = (
            capo_workmail.types.device_type_list.serialize_aws_json_1_1(
                value["device_types"]
            )
        )
    if "not_device_types" in value:
        import capo_workmail.types.device_type_list

        out["NotDeviceTypes"] = (
            capo_workmail.types.device_type_list.serialize_aws_json_1_1(
                value["not_device_types"]
            )
        )
    if "device_models" in value:
        import capo_workmail.types.device_model_list

        out["DeviceModels"] = (
            capo_workmail.types.device_model_list.serialize_aws_json_1_1(
                value["device_models"]
            )
        )
    if "not_device_models" in value:
        import capo_workmail.types.device_model_list

        out["NotDeviceModels"] = (
            capo_workmail.types.device_model_list.serialize_aws_json_1_1(
                value["not_device_models"]
            )
        )
    if "device_operating_systems" in value:
        import capo_workmail.types.device_operating_system_list

        out["DeviceOperatingSystems"] = (
            capo_workmail.types.device_operating_system_list.serialize_aws_json_1_1(
                value["device_operating_systems"]
            )
        )
    if "not_device_operating_systems" in value:
        import capo_workmail.types.device_operating_system_list

        out["NotDeviceOperatingSystems"] = (
            capo_workmail.types.device_operating_system_list.serialize_aws_json_1_1(
                value["not_device_operating_systems"]
            )
        )
    if "device_user_agents" in value:
        import capo_workmail.types.device_user_agent_list

        out["DeviceUserAgents"] = (
            capo_workmail.types.device_user_agent_list.serialize_aws_json_1_1(
                value["device_user_agents"]
            )
        )
    if "not_device_user_agents" in value:
        import capo_workmail.types.device_user_agent_list

        out["NotDeviceUserAgents"] = (
            capo_workmail.types.device_user_agent_list.serialize_aws_json_1_1(
                value["not_device_user_agents"]
            )
        )
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


def deserialize_aws_json_1_1(data: dict) -> MobileDeviceAccessRule:
    out: MobileDeviceAccessRule = {}  # type: ignore[typeddict-item]
    if "MobileDeviceAccessRuleId" in data:
        out["mobile_device_access_rule_id"] = data["MobileDeviceAccessRuleId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Effect" in data:
        import capo_workmail.types.mobile_device_access_rule_effect

        out["effect"] = (
            capo_workmail.types.mobile_device_access_rule_effect.deserialize_aws_json_1_1(
                data["Effect"]
            )
        )
    if "DeviceTypes" in data:
        import capo_workmail.types.device_type_list

        out["device_types"] = (
            capo_workmail.types.device_type_list.deserialize_aws_json_1_1(
                data["DeviceTypes"]
            )
        )
    if "NotDeviceTypes" in data:
        import capo_workmail.types.device_type_list

        out["not_device_types"] = (
            capo_workmail.types.device_type_list.deserialize_aws_json_1_1(
                data["NotDeviceTypes"]
            )
        )
    if "DeviceModels" in data:
        import capo_workmail.types.device_model_list

        out["device_models"] = (
            capo_workmail.types.device_model_list.deserialize_aws_json_1_1(
                data["DeviceModels"]
            )
        )
    if "NotDeviceModels" in data:
        import capo_workmail.types.device_model_list

        out["not_device_models"] = (
            capo_workmail.types.device_model_list.deserialize_aws_json_1_1(
                data["NotDeviceModels"]
            )
        )
    if "DeviceOperatingSystems" in data:
        import capo_workmail.types.device_operating_system_list

        out["device_operating_systems"] = (
            capo_workmail.types.device_operating_system_list.deserialize_aws_json_1_1(
                data["DeviceOperatingSystems"]
            )
        )
    if "NotDeviceOperatingSystems" in data:
        import capo_workmail.types.device_operating_system_list

        out["not_device_operating_systems"] = (
            capo_workmail.types.device_operating_system_list.deserialize_aws_json_1_1(
                data["NotDeviceOperatingSystems"]
            )
        )
    if "DeviceUserAgents" in data:
        import capo_workmail.types.device_user_agent_list

        out["device_user_agents"] = (
            capo_workmail.types.device_user_agent_list.deserialize_aws_json_1_1(
                data["DeviceUserAgents"]
            )
        )
    if "NotDeviceUserAgents" in data:
        import capo_workmail.types.device_user_agent_list

        out["not_device_user_agents"] = (
            capo_workmail.types.device_user_agent_list.deserialize_aws_json_1_1(
                data["NotDeviceUserAgents"]
            )
        )
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
