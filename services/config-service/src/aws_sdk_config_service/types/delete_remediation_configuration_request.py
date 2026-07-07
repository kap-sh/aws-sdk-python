"""Generated from Smithy shape ``com.amazonaws.configservice#DeleteRemediationConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.config_rule_name
    import aws_sdk_config_service.types.string


class DeleteRemediationConfigurationRequest(TypedDict, closed=True):
    config_rule_name: "aws_sdk_config_service.types.config_rule_name.ConfigRuleName"
    """<p>The name of the Config rule for which you want to delete remediation configuration.</p>"""
    resource_type: NotRequired["aws_sdk_config_service.types.string.String"]
    """<p>The type of a resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRemediationConfigurationRequest) -> dict:
    out: dict = {}
    out["ConfigRuleName"] = value["config_rule_name"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRemediationConfigurationRequest:
    out: DeleteRemediationConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "ConfigRuleName" in data:
        out["config_rule_name"] = data["ConfigRuleName"]
    else:
        raise DeserializationError(
            "DeleteRemediationConfigurationRequest.config_rule_name required"
        )
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    return out
