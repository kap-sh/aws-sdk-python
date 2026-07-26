"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#StartCodeInterpreterSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.certificates
    import capo_bedrock_agentcore.types.client_token
    import capo_bedrock_agentcore.types.code_interpreter_session_timeout
    import capo_bedrock_agentcore.types.name


class StartCodeInterpreterSessionRequest(TypedDict, closed=True):
    trace_id: NotRequired["str"]
    """<p>The trace identifier for request tracking.</p>"""
    trace_parent: NotRequired["str"]
    """<p>The parent trace information for distributed tracing.</p>"""
    code_interpreter_identifier: "str"
    """<p>The unique identifier of the code interpreter to use for this session. This identifier specifies which code interpreter environment to initialize for the session.</p>"""
    name: NotRequired["capo_bedrock_agentcore.types.name.Name"]
    """<p>The name of the code interpreter session. This name helps you identify and manage the session. The name does not need to be unique.</p>"""
    session_timeout_seconds: "capo_bedrock_agentcore.types.code_interpreter_session_timeout.CodeInterpreterSessionTimeout"
    """<p>The duration in seconds (time-to-live) after which the session automatically terminates, regardless of ongoing activity. Defaults to 900 seconds (15 minutes). Recommended minimum: 60 seconds. Maximum allowed: 28,800 seconds (8 hours).</p>"""
    certificates: NotRequired["capo_bedrock_agentcore.types.certificates.Certificates"]
    """<p>A list of certificates to install in the code interpreter session.</p>"""
    client_token: NotRequired["capo_bedrock_agentcore.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error. This parameter helps prevent the creation of duplicate sessions if there are temporary network issues.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartCodeInterpreterSessionRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    out["sessionTimeoutSeconds"] = value.get("session_timeout_seconds", 900)
    if "certificates" in value:
        import capo_bedrock_agentcore.types.certificates

        out["certificates"] = capo_bedrock_agentcore.types.certificates.serialize_json(
            value["certificates"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartCodeInterpreterSessionRequest:
    out: StartCodeInterpreterSessionRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "sessionTimeoutSeconds" in data:
        out["session_timeout_seconds"] = data["sessionTimeoutSeconds"]
    else:
        out["session_timeout_seconds"] = 900
    if "certificates" in data:
        import capo_bedrock_agentcore.types.certificates

        out["certificates"] = (
            capo_bedrock_agentcore.types.certificates.deserialize_json(
                data["certificates"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
