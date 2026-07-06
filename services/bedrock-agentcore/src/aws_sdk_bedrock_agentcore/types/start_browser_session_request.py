"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#StartBrowserSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.browser_enterprise_policies
    import aws_sdk_bedrock_agentcore.types.browser_extensions
    import aws_sdk_bedrock_agentcore.types.browser_profile_configuration
    import aws_sdk_bedrock_agentcore.types.browser_session_timeout
    import aws_sdk_bedrock_agentcore.types.certificates
    import aws_sdk_bedrock_agentcore.types.client_token
    import aws_sdk_bedrock_agentcore.types.name
    import aws_sdk_bedrock_agentcore.types.proxy_configuration
    import aws_sdk_bedrock_agentcore.types.view_port


class StartBrowserSessionRequest(TypedDict, closed=True):
    trace_id: NotRequired["str"]
    """<p>The trace identifier for request tracking.</p>"""
    trace_parent: NotRequired["str"]
    """<p>The parent trace information for distributed tracing.</p>"""
    browser_identifier: "str"
    """<p>The unique identifier of the browser to use for this session. This identifier specifies which browser environment to initialize for the session.</p>"""
    name: NotRequired["aws_sdk_bedrock_agentcore.types.name.Name"]
    """<p>The name of the browser session. This name helps you identify and manage the session. The name does not need to be unique.</p>"""
    session_timeout_seconds: (
        "aws_sdk_bedrock_agentcore.types.browser_session_timeout.BrowserSessionTimeout"
    )
    """<p>The duration in seconds (time-to-live) after which the session automatically terminates, regardless of ongoing activity. Defaults to 3600 seconds (1 hour). Recommended minimum: 60 seconds. Maximum allowed: 28,800 seconds (8 hours).</p>"""
    view_port: NotRequired["aws_sdk_bedrock_agentcore.types.view_port.ViewPort"]
    """<p>The dimensions of the browser viewport for this session. This determines the visible area of the web content and affects how web pages are rendered. If not specified, Amazon Bedrock AgentCore uses a default viewport size.</p>"""
    extensions: NotRequired[
        "aws_sdk_bedrock_agentcore.types.browser_extensions.BrowserExtensions"
    ]
    """<p>A list of browser extensions to load into the browser session.</p>"""
    profile_configuration: NotRequired[
        "aws_sdk_bedrock_agentcore.types.browser_profile_configuration.BrowserProfileConfiguration"
    ]
    """<p>The browser profile configuration to use for this session. A browser profile contains persistent data such as cookies and local storage that can be reused across multiple browser sessions. If specified, the session initializes with the profile's stored data, enabling continuity for tasks that require authentication or personalized settings.</p>"""
    proxy_configuration: NotRequired[
        "aws_sdk_bedrock_agentcore.types.proxy_configuration.ProxyConfiguration"
    ]
    """<p>Optional proxy configuration for routing browser traffic through customer-specified proxy servers. When provided, enables HTTP Basic authentication via Amazon Web Services Secrets Manager and domain-based routing rules. Requires <code>secretsmanager:GetSecretValue</code> IAM permission for the specified secret ARNs.</p>"""
    enterprise_policies: NotRequired[
        "aws_sdk_bedrock_agentcore.types.browser_enterprise_policies.BrowserEnterprisePolicies"
    ]
    """<p>A list of files containing enterprise policies for the browser.</p>"""
    certificates: NotRequired[
        "aws_sdk_bedrock_agentcore.types.certificates.Certificates"
    ]
    """<p>A list of certificates to install in the browser session.</p>"""
    client_token: NotRequired[
        "aws_sdk_bedrock_agentcore.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error. This parameter helps prevent the creation of duplicate sessions if there are temporary network issues.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartBrowserSessionRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    out["sessionTimeoutSeconds"] = value.get("session_timeout_seconds", 3600)
    if "view_port" in value:
        import aws_sdk_bedrock_agentcore.types.view_port

        out["viewPort"] = aws_sdk_bedrock_agentcore.types.view_port.serialize_json(
            value["view_port"]
        )
    if "extensions" in value:
        import aws_sdk_bedrock_agentcore.types.browser_extensions

        out["extensions"] = (
            aws_sdk_bedrock_agentcore.types.browser_extensions.serialize_json(
                value["extensions"]
            )
        )
    if "profile_configuration" in value:
        import aws_sdk_bedrock_agentcore.types.browser_profile_configuration

        out["profileConfiguration"] = (
            aws_sdk_bedrock_agentcore.types.browser_profile_configuration.serialize_json(
                value["profile_configuration"]
            )
        )
    if "proxy_configuration" in value:
        import aws_sdk_bedrock_agentcore.types.proxy_configuration

        out["proxyConfiguration"] = (
            aws_sdk_bedrock_agentcore.types.proxy_configuration.serialize_json(
                value["proxy_configuration"]
            )
        )
    if "enterprise_policies" in value:
        import aws_sdk_bedrock_agentcore.types.browser_enterprise_policies

        out["enterprisePolicies"] = (
            aws_sdk_bedrock_agentcore.types.browser_enterprise_policies.serialize_json(
                value["enterprise_policies"]
            )
        )
    if "certificates" in value:
        import aws_sdk_bedrock_agentcore.types.certificates

        out["certificates"] = (
            aws_sdk_bedrock_agentcore.types.certificates.serialize_json(
                value["certificates"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartBrowserSessionRequest:
    out: StartBrowserSessionRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "sessionTimeoutSeconds" in data:
        out["session_timeout_seconds"] = data["sessionTimeoutSeconds"]
    else:
        out["session_timeout_seconds"] = 3600
    if "viewPort" in data:
        import aws_sdk_bedrock_agentcore.types.view_port

        out["view_port"] = aws_sdk_bedrock_agentcore.types.view_port.deserialize_json(
            data["viewPort"]
        )
    if "extensions" in data:
        import aws_sdk_bedrock_agentcore.types.browser_extensions

        out["extensions"] = (
            aws_sdk_bedrock_agentcore.types.browser_extensions.deserialize_json(
                data["extensions"]
            )
        )
    if "profileConfiguration" in data:
        import aws_sdk_bedrock_agentcore.types.browser_profile_configuration

        out["profile_configuration"] = (
            aws_sdk_bedrock_agentcore.types.browser_profile_configuration.deserialize_json(
                data["profileConfiguration"]
            )
        )
    if "proxyConfiguration" in data:
        import aws_sdk_bedrock_agentcore.types.proxy_configuration

        out["proxy_configuration"] = (
            aws_sdk_bedrock_agentcore.types.proxy_configuration.deserialize_json(
                data["proxyConfiguration"]
            )
        )
    if "enterprisePolicies" in data:
        import aws_sdk_bedrock_agentcore.types.browser_enterprise_policies

        out["enterprise_policies"] = (
            aws_sdk_bedrock_agentcore.types.browser_enterprise_policies.deserialize_json(
                data["enterprisePolicies"]
            )
        )
    if "certificates" in data:
        import aws_sdk_bedrock_agentcore.types.certificates

        out["certificates"] = (
            aws_sdk_bedrock_agentcore.types.certificates.deserialize_json(
                data["certificates"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
