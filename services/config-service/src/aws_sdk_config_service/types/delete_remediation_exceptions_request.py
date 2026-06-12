"""Generated from Smithy shape ``com.amazonaws.configservice#DeleteRemediationExceptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.config_rule_name
    import aws_sdk_config_service.types.remediation_exception_resource_keys


class DeleteRemediationExceptionsRequest(TypedDict):
    config_rule_name: "aws_sdk_config_service.types.config_rule_name.ConfigRuleName"
    """<p>The name of the Config rule for which you want to delete remediation exception configuration.</p>"""
    resource_keys: "aws_sdk_config_service.types.remediation_exception_resource_keys.RemediationExceptionResourceKeys"
    """<p>An exception list of resource exception keys to be processed with the current request. Config adds exception for each resource key. For example, Config adds 3 exceptions for 3 resource keys. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRemediationExceptionsRequest) -> dict:
    out: dict = {}
    out["ConfigRuleName"] = value["config_rule_name"]
    import aws_sdk_config_service.types.remediation_exception_resource_keys

    out["ResourceKeys"] = (
        aws_sdk_config_service.types.remediation_exception_resource_keys.serialize_aws_json_1_1(
            value["resource_keys"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRemediationExceptionsRequest:
    out: DeleteRemediationExceptionsRequest = {}  # type: ignore[typeddict-item]
    if "ConfigRuleName" in data:
        out["config_rule_name"] = data["ConfigRuleName"]
    else:
        raise DeserializationError(
            "DeleteRemediationExceptionsRequest.config_rule_name required"
        )
    if "ResourceKeys" in data:
        import aws_sdk_config_service.types.remediation_exception_resource_keys

        out["resource_keys"] = (
            aws_sdk_config_service.types.remediation_exception_resource_keys.deserialize_aws_json_1_1(
                data["ResourceKeys"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteRemediationExceptionsRequest.resource_keys required"
        )
    return out
