"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeRemediationExceptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.config_rule_name
    import aws_sdk_config_service.types.limit
    import aws_sdk_config_service.types.remediation_exception_resource_keys
    import aws_sdk_config_service.types.string


class DescribeRemediationExceptionsRequest(TypedDict):
    config_rule_name: "aws_sdk_config_service.types.config_rule_name.ConfigRuleName"
    """<p>The name of the Config rule.</p>"""
    resource_keys: NotRequired[
        "aws_sdk_config_service.types.remediation_exception_resource_keys.RemediationExceptionResourceKeys"
    ]
    """<p>An exception list of resource exception keys to be processed with the current request. Config adds exception for each resource key. For example, Config adds 3 exceptions for 3 resource keys. </p>"""
    limit: "aws_sdk_config_service.types.limit.Limit"
    """<p>The maximum number of RemediationExceptionResourceKey returned on each page. The default is 25. If you specify 0, Config uses the default.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.string.String"]
    """<p>The <code>nextToken</code> string returned in a previous request that you use to request the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRemediationExceptionsRequest) -> dict:
    out: dict = {}
    out["ConfigRuleName"] = value["config_rule_name"]
    if "resource_keys" in value:
        import aws_sdk_config_service.types.remediation_exception_resource_keys

        out["ResourceKeys"] = (
            aws_sdk_config_service.types.remediation_exception_resource_keys.serialize_aws_json_1_1(
                value["resource_keys"]
            )
        )
    out["Limit"] = value.get("limit", 0)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRemediationExceptionsRequest:
    out: DescribeRemediationExceptionsRequest = {}  # type: ignore[typeddict-item]
    if "ConfigRuleName" in data:
        out["config_rule_name"] = data["ConfigRuleName"]
    else:
        raise DeserializationError(
            "DescribeRemediationExceptionsRequest.config_rule_name required"
        )
    if "ResourceKeys" in data:
        import aws_sdk_config_service.types.remediation_exception_resource_keys

        out["resource_keys"] = (
            aws_sdk_config_service.types.remediation_exception_resource_keys.deserialize_aws_json_1_1(
                data["ResourceKeys"]
            )
        )
    if "Limit" in data:
        out["limit"] = data["Limit"]
    else:
        out["limit"] = 0
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
