"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetBrowserResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.browser_arn
    import aws_sdk_bedrock_agentcore_control.types.browser_enterprise_policies
    import aws_sdk_bedrock_agentcore_control.types.browser_id
    import aws_sdk_bedrock_agentcore_control.types.browser_network_configuration
    import aws_sdk_bedrock_agentcore_control.types.browser_signing_config_output
    import aws_sdk_bedrock_agentcore_control.types.browser_status
    import aws_sdk_bedrock_agentcore_control.types.certificates
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    import aws_sdk_bedrock_agentcore_control.types.description
    import aws_sdk_bedrock_agentcore_control.types.recording_config
    import aws_sdk_bedrock_agentcore_control.types.role_arn
    import aws_sdk_bedrock_agentcore_control.types.sandbox_name

class GetBrowserResponse(TypedDict):
    browser_id: "aws_sdk_bedrock_agentcore_control.types.browser_id.BrowserId"
    """<p>The unique identifier of the browser.</p>"""
    browser_arn: "aws_sdk_bedrock_agentcore_control.types.browser_arn.BrowserArn"
    """<p>The Amazon Resource Name (ARN) of the browser.</p>"""
    name: "aws_sdk_bedrock_agentcore_control.types.sandbox_name.SandboxName"
    """<p>The name of the browser.</p>"""
    description: NotRequired["aws_sdk_bedrock_agentcore_control.types.description.Description"]
    """<p>The description of the browser.</p>"""
    execution_role_arn: NotRequired["aws_sdk_bedrock_agentcore_control.types.role_arn.RoleArn"]
    """<p>The IAM role ARN that provides permissions for the browser.</p>"""
    network_configuration: "aws_sdk_bedrock_agentcore_control.types.browser_network_configuration.BrowserNetworkConfiguration"
    recording: NotRequired["aws_sdk_bedrock_agentcore_control.types.recording_config.RecordingConfig"]
    browser_signing: NotRequired["aws_sdk_bedrock_agentcore_control.types.browser_signing_config_output.BrowserSigningConfigOutput"]
    """<p>The browser signing configuration that shows whether cryptographic agent identification is enabled for web bot authentication.</p>"""
    enterprise_policies: NotRequired["aws_sdk_bedrock_agentcore_control.types.browser_enterprise_policies.BrowserEnterprisePolicies"]
    """<p>The list of enterprise policy files configured for the browser.</p>"""
    certificates: NotRequired["aws_sdk_bedrock_agentcore_control.types.certificates.Certificates"]
    """<p>The list of certificates configured for the browser.</p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.browser_status.BrowserStatus"
    """<p>The current status of the browser.</p>"""
    failure_reason: NotRequired["str"]
    """<p>The reason for failure if the browser is in a failed state.</p>"""
    created_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the browser was created.</p>"""
    last_updated_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the browser was last updated.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetBrowserResponse) -> dict:
    out: dict = {}
    out["browserId"] = value["browser_id"]
    out["browserArn"] = value["browser_arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "execution_role_arn" in value:
        out["executionRoleArn"] = value["execution_role_arn"]
    import aws_sdk_bedrock_agentcore_control.types.browser_network_configuration
    out["networkConfiguration"] = aws_sdk_bedrock_agentcore_control.types.browser_network_configuration.serialize_json(value["network_configuration"])
    if "recording" in value:
        import aws_sdk_bedrock_agentcore_control.types.recording_config
        out["recording"] = aws_sdk_bedrock_agentcore_control.types.recording_config.serialize_json(value["recording"])
    if "browser_signing" in value:
        import aws_sdk_bedrock_agentcore_control.types.browser_signing_config_output
        out["browserSigning"] = aws_sdk_bedrock_agentcore_control.types.browser_signing_config_output.serialize_json(value["browser_signing"])
    if "enterprise_policies" in value:
        import aws_sdk_bedrock_agentcore_control.types.browser_enterprise_policies
        out["enterprisePolicies"] = aws_sdk_bedrock_agentcore_control.types.browser_enterprise_policies.serialize_json(value["enterprise_policies"])
    if "certificates" in value:
        import aws_sdk_bedrock_agentcore_control.types.certificates
        out["certificates"] = aws_sdk_bedrock_agentcore_control.types.certificates.serialize_json(value["certificates"])
    import aws_sdk_bedrock_agentcore_control.types.browser_status
    out["status"] = aws_sdk_bedrock_agentcore_control.types.browser_status.serialize_json(value["status"])
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    out["createdAt"] = aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(value["created_at"])
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    out["lastUpdatedAt"] = aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(value["last_updated_at"])
    return out


def deserialize_json(data: dict) -> GetBrowserResponse:
    out: GetBrowserResponse = {}  # type: ignore[typeddict-item]
    if "browserId" in data:
        out["browser_id"] = data["browserId"]
    else:
        raise DeserializationError("GetBrowserResponse.browser_id required")
    if "browserArn" in data:
        out["browser_arn"] = data["browserArn"]
    else:
        raise DeserializationError("GetBrowserResponse.browser_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetBrowserResponse.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "executionRoleArn" in data:
        out["execution_role_arn"] = data["executionRoleArn"]
    if "networkConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.browser_network_configuration
        out["network_configuration"] = aws_sdk_bedrock_agentcore_control.types.browser_network_configuration.deserialize_json(data["networkConfiguration"])
    else:
        raise DeserializationError("GetBrowserResponse.network_configuration required")
    if "recording" in data:
        import aws_sdk_bedrock_agentcore_control.types.recording_config
        out["recording"] = aws_sdk_bedrock_agentcore_control.types.recording_config.deserialize_json(data["recording"])
    if "browserSigning" in data:
        import aws_sdk_bedrock_agentcore_control.types.browser_signing_config_output
        out["browser_signing"] = aws_sdk_bedrock_agentcore_control.types.browser_signing_config_output.deserialize_json(data["browserSigning"])
    if "enterprisePolicies" in data:
        import aws_sdk_bedrock_agentcore_control.types.browser_enterprise_policies
        out["enterprise_policies"] = aws_sdk_bedrock_agentcore_control.types.browser_enterprise_policies.deserialize_json(data["enterprisePolicies"])
    if "certificates" in data:
        import aws_sdk_bedrock_agentcore_control.types.certificates
        out["certificates"] = aws_sdk_bedrock_agentcore_control.types.certificates.deserialize_json(data["certificates"])
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.browser_status
        out["status"] = aws_sdk_bedrock_agentcore_control.types.browser_status.deserialize_json(data["status"])
    else:
        raise DeserializationError("GetBrowserResponse.status required")
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp
        out["created_at"] = aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(data["createdAt"])
    else:
        raise DeserializationError("GetBrowserResponse.created_at required")
    if "lastUpdatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp
        out["last_updated_at"] = aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(data["lastUpdatedAt"])
    else:
        raise DeserializationError("GetBrowserResponse.last_updated_at required")
    return out