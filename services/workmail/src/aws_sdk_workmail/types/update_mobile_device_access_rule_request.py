"""Generated from Smithy shape ``com.amazonaws.workmail#UpdateMobileDeviceAccessRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.device_model_list
    import aws_sdk_workmail.types.device_operating_system_list
    import aws_sdk_workmail.types.device_type_list
    import aws_sdk_workmail.types.device_user_agent_list
    import aws_sdk_workmail.types.mobile_device_access_rule_description
    import aws_sdk_workmail.types.mobile_device_access_rule_effect
    import aws_sdk_workmail.types.mobile_device_access_rule_id
    import aws_sdk_workmail.types.mobile_device_access_rule_name
    import aws_sdk_workmail.types.organization_id


class UpdateMobileDeviceAccessRuleRequest(TypedDict):
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>The WorkMail organization under which the rule will be updated.</p>"""
    mobile_device_access_rule_id: (
        "aws_sdk_workmail.types.mobile_device_access_rule_id.MobileDeviceAccessRuleId"
    )
    """<p>The identifier of the rule to be updated.</p>"""
    name: "aws_sdk_workmail.types.mobile_device_access_rule_name.MobileDeviceAccessRuleName"
    """<p>The updated rule name.</p>"""
    description: NotRequired[
        "aws_sdk_workmail.types.mobile_device_access_rule_description.MobileDeviceAccessRuleDescription"
    ]
    """<p>The updated rule description.</p>"""
    effect: "aws_sdk_workmail.types.mobile_device_access_rule_effect.MobileDeviceAccessRuleEffect"
    """<p>The effect of the rule when it matches. Allowed values are <code>ALLOW</code> or <code>DENY</code>.</p>"""
    device_types: NotRequired["aws_sdk_workmail.types.device_type_list.DeviceTypeList"]
    """<p>Device types that the updated rule will match.</p>"""
    not_device_types: NotRequired[
        "aws_sdk_workmail.types.device_type_list.DeviceTypeList"
    ]
    """<p>Device types that the updated rule <b>will not</b> match. All other device types will match.</p>"""
    device_models: NotRequired[
        "aws_sdk_workmail.types.device_model_list.DeviceModelList"
    ]
    """<p>Device models that the updated rule will match.</p>"""
    not_device_models: NotRequired[
        "aws_sdk_workmail.types.device_model_list.DeviceModelList"
    ]
    """<p>Device models that the updated rule <b>will not</b> match. All other device models will match.</p>"""
    device_operating_systems: NotRequired[
        "aws_sdk_workmail.types.device_operating_system_list.DeviceOperatingSystemList"
    ]
    """<p>Device operating systems that the updated rule will match.</p>"""
    not_device_operating_systems: NotRequired[
        "aws_sdk_workmail.types.device_operating_system_list.DeviceOperatingSystemList"
    ]
    """<p>Device operating systems that the updated rule <b>will not</b> match. All other device operating systems will match.</p>"""
    device_user_agents: NotRequired[
        "aws_sdk_workmail.types.device_user_agent_list.DeviceUserAgentList"
    ]
    """<p>User agents that the updated rule will match.</p>"""
    not_device_user_agents: NotRequired[
        "aws_sdk_workmail.types.device_user_agent_list.DeviceUserAgentList"
    ]
    """<p>User agents that the updated rule <b>will not</b> match. All other user agents will match.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateMobileDeviceAccessRuleRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["MobileDeviceAccessRuleId"] = value["mobile_device_access_rule_id"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateMobileDeviceAccessRuleRequest:
    out: UpdateMobileDeviceAccessRuleRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "UpdateMobileDeviceAccessRuleRequest.organization_id required"
        )
    if "MobileDeviceAccessRuleId" in data:
        out["mobile_device_access_rule_id"] = data["MobileDeviceAccessRuleId"]
    else:
        raise DeserializationError(
            "UpdateMobileDeviceAccessRuleRequest.mobile_device_access_rule_id required"
        )
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateMobileDeviceAccessRuleRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Effect" in data:
        import aws_sdk_workmail.types.mobile_device_access_rule_effect

        out["effect"] = (
            aws_sdk_workmail.types.mobile_device_access_rule_effect.deserialize_aws_json_1_1(
                data["Effect"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateMobileDeviceAccessRuleRequest.effect required"
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
    return out
