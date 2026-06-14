"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetBrowserSessionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.browser_enterprise_policies
    import aws_sdk_bedrock_agentcore.types.browser_extensions
    import aws_sdk_bedrock_agentcore.types.browser_profile_configuration
    import aws_sdk_bedrock_agentcore.types.browser_session_id
    import aws_sdk_bedrock_agentcore.types.browser_session_status
    import aws_sdk_bedrock_agentcore.types.browser_session_stream
    import aws_sdk_bedrock_agentcore.types.browser_session_timeout
    import aws_sdk_bedrock_agentcore.types.certificates
    import aws_sdk_bedrock_agentcore.types.date_timestamp
    import aws_sdk_bedrock_agentcore.types.name
    import aws_sdk_bedrock_agentcore.types.proxy_configuration
    import aws_sdk_bedrock_agentcore.types.view_port


class GetBrowserSessionResponse(TypedDict):
    browser_identifier: "str"
    """<p>The identifier of the browser.</p>"""
    session_id: "aws_sdk_bedrock_agentcore.types.browser_session_id.BrowserSessionId"
    """<p>The identifier of the browser session.</p>"""
    name: NotRequired["aws_sdk_bedrock_agentcore.types.name.Name"]
    """<p>The name of the browser session.</p>"""
    created_at: "aws_sdk_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    """<p>The time at which the browser session was created.</p>"""
    view_port: NotRequired["aws_sdk_bedrock_agentcore.types.view_port.ViewPort"]
    extensions: NotRequired[
        "aws_sdk_bedrock_agentcore.types.browser_extensions.BrowserExtensions"
    ]
    """<p>The list of browser extensions that are configured in the browser session.</p>"""
    enterprise_policies: NotRequired[
        "aws_sdk_bedrock_agentcore.types.browser_enterprise_policies.BrowserEnterprisePolicies"
    ]
    """<p>A list of files containing enterprise policies for the browser session.</p>"""
    profile_configuration: NotRequired[
        "aws_sdk_bedrock_agentcore.types.browser_profile_configuration.BrowserProfileConfiguration"
    ]
    """<p>The browser profile configuration associated with this session. Contains the profile identifier that links to persistent browser data such as cookies and local storage.</p>"""
    session_timeout_seconds: NotRequired[
        "aws_sdk_bedrock_agentcore.types.browser_session_timeout.BrowserSessionTimeout"
    ]
    """<p>The timeout period for the browser session in seconds.</p>"""
    status: NotRequired[
        "aws_sdk_bedrock_agentcore.types.browser_session_status.BrowserSessionStatus"
    ]
    """<p>The current status of the browser session. Possible values include ACTIVE, STOPPING, and STOPPED.</p>"""
    streams: NotRequired[
        "aws_sdk_bedrock_agentcore.types.browser_session_stream.BrowserSessionStream"
    ]
    """<p>The streams associated with this browser session. These include the automation stream and live view stream.</p>"""
    proxy_configuration: NotRequired[
        "aws_sdk_bedrock_agentcore.types.proxy_configuration.ProxyConfiguration"
    ]
    """<p>The active proxy configuration for this browser session. This field is only present if proxy configuration was provided when the session was started using <code>StartBrowserSession</code>. The configuration includes proxy servers, domain bypass rules and the proxy authentication credentials.</p>"""
    certificates: NotRequired[
        "aws_sdk_bedrock_agentcore.types.certificates.Certificates"
    ]
    """<p>The list of certificates installed in the browser session.</p>"""
    session_replay_artifact: NotRequired["str"]
    """<p>The artifact containing the session replay information.</p>"""
    last_updated_at: NotRequired[
        "aws_sdk_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    ]
    """<p>The time at which the browser session was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBrowserSessionResponse) -> dict:
    out: dict = {}
    out["browserIdentifier"] = value["browser_identifier"]
    out["sessionId"] = value["session_id"]
    if "name" in value:
        out["name"] = value["name"]
    import aws_sdk_bedrock_agentcore.types.date_timestamp

    out["createdAt"] = aws_sdk_bedrock_agentcore.types.date_timestamp.serialize_json(
        value["created_at"]
    )
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
    if "enterprise_policies" in value:
        import aws_sdk_bedrock_agentcore.types.browser_enterprise_policies

        out["enterprisePolicies"] = (
            aws_sdk_bedrock_agentcore.types.browser_enterprise_policies.serialize_json(
                value["enterprise_policies"]
            )
        )
    if "profile_configuration" in value:
        import aws_sdk_bedrock_agentcore.types.browser_profile_configuration

        out["profileConfiguration"] = (
            aws_sdk_bedrock_agentcore.types.browser_profile_configuration.serialize_json(
                value["profile_configuration"]
            )
        )
    if "session_timeout_seconds" in value:
        out["sessionTimeoutSeconds"] = value["session_timeout_seconds"]
    if "status" in value:
        import aws_sdk_bedrock_agentcore.types.browser_session_status

        out["status"] = (
            aws_sdk_bedrock_agentcore.types.browser_session_status.serialize_json(
                value["status"]
            )
        )
    if "streams" in value:
        import aws_sdk_bedrock_agentcore.types.browser_session_stream

        out["streams"] = (
            aws_sdk_bedrock_agentcore.types.browser_session_stream.serialize_json(
                value["streams"]
            )
        )
    if "proxy_configuration" in value:
        import aws_sdk_bedrock_agentcore.types.proxy_configuration

        out["proxyConfiguration"] = (
            aws_sdk_bedrock_agentcore.types.proxy_configuration.serialize_json(
                value["proxy_configuration"]
            )
        )
    if "certificates" in value:
        import aws_sdk_bedrock_agentcore.types.certificates

        out["certificates"] = (
            aws_sdk_bedrock_agentcore.types.certificates.serialize_json(
                value["certificates"]
            )
        )
    if "session_replay_artifact" in value:
        out["sessionReplayArtifact"] = value["session_replay_artifact"]
    if "last_updated_at" in value:
        import aws_sdk_bedrock_agentcore.types.date_timestamp

        out["lastUpdatedAt"] = (
            aws_sdk_bedrock_agentcore.types.date_timestamp.serialize_json(
                value["last_updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetBrowserSessionResponse:
    out: GetBrowserSessionResponse = {}  # type: ignore[typeddict-item]
    if "browserIdentifier" in data:
        out["browser_identifier"] = data["browserIdentifier"]
    else:
        raise DeserializationError(
            "GetBrowserSessionResponse.browser_identifier required"
        )
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("GetBrowserSessionResponse.session_id required")
    if "name" in data:
        out["name"] = data["name"]
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore.types.date_timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("GetBrowserSessionResponse.created_at required")
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
    if "enterprisePolicies" in data:
        import aws_sdk_bedrock_agentcore.types.browser_enterprise_policies

        out["enterprise_policies"] = (
            aws_sdk_bedrock_agentcore.types.browser_enterprise_policies.deserialize_json(
                data["enterprisePolicies"]
            )
        )
    if "profileConfiguration" in data:
        import aws_sdk_bedrock_agentcore.types.browser_profile_configuration

        out["profile_configuration"] = (
            aws_sdk_bedrock_agentcore.types.browser_profile_configuration.deserialize_json(
                data["profileConfiguration"]
            )
        )
    if "sessionTimeoutSeconds" in data:
        out["session_timeout_seconds"] = data["sessionTimeoutSeconds"]
    if "status" in data:
        import aws_sdk_bedrock_agentcore.types.browser_session_status

        out["status"] = (
            aws_sdk_bedrock_agentcore.types.browser_session_status.deserialize_json(
                data["status"]
            )
        )
    if "streams" in data:
        import aws_sdk_bedrock_agentcore.types.browser_session_stream

        out["streams"] = (
            aws_sdk_bedrock_agentcore.types.browser_session_stream.deserialize_json(
                data["streams"]
            )
        )
    if "proxyConfiguration" in data:
        import aws_sdk_bedrock_agentcore.types.proxy_configuration

        out["proxy_configuration"] = (
            aws_sdk_bedrock_agentcore.types.proxy_configuration.deserialize_json(
                data["proxyConfiguration"]
            )
        )
    if "certificates" in data:
        import aws_sdk_bedrock_agentcore.types.certificates

        out["certificates"] = (
            aws_sdk_bedrock_agentcore.types.certificates.deserialize_json(
                data["certificates"]
            )
        )
    if "sessionReplayArtifact" in data:
        out["session_replay_artifact"] = data["sessionReplayArtifact"]
    if "lastUpdatedAt" in data:
        import aws_sdk_bedrock_agentcore.types.date_timestamp

        out["last_updated_at"] = (
            aws_sdk_bedrock_agentcore.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    return out
