"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MetadataConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.allowed_query_parameters
    import capo_bedrock_agentcore_control.types.allowed_request_headers
    import capo_bedrock_agentcore_control.types.allowed_response_headers


class MetadataConfiguration(TypedDict, closed=True):
    allowed_request_headers: NotRequired[
        "capo_bedrock_agentcore_control.types.allowed_request_headers.AllowedRequestHeaders"
    ]
    """<p>A list of HTTP headers that are allowed to be propagated from incoming client requests to the target.</p>"""
    allowed_query_parameters: NotRequired[
        "capo_bedrock_agentcore_control.types.allowed_query_parameters.AllowedQueryParameters"
    ]
    """<p>A list of URL query parameters that are allowed to be propagated from incoming gateway URL to the target.</p>"""
    allowed_response_headers: NotRequired[
        "capo_bedrock_agentcore_control.types.allowed_response_headers.AllowedResponseHeaders"
    ]
    """<p>A list of HTTP headers that are allowed to be propagated from the target response back to the client.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetadataConfiguration) -> dict:
    out: dict = {}
    if "allowed_request_headers" in value:
        import capo_bedrock_agentcore_control.types.allowed_request_headers

        out["allowedRequestHeaders"] = (
            capo_bedrock_agentcore_control.types.allowed_request_headers.serialize_json(
                value["allowed_request_headers"]
            )
        )
    if "allowed_query_parameters" in value:
        import capo_bedrock_agentcore_control.types.allowed_query_parameters

        out["allowedQueryParameters"] = (
            capo_bedrock_agentcore_control.types.allowed_query_parameters.serialize_json(
                value["allowed_query_parameters"]
            )
        )
    if "allowed_response_headers" in value:
        import capo_bedrock_agentcore_control.types.allowed_response_headers

        out["allowedResponseHeaders"] = (
            capo_bedrock_agentcore_control.types.allowed_response_headers.serialize_json(
                value["allowed_response_headers"]
            )
        )
    return out


def deserialize_json(data: dict) -> MetadataConfiguration:
    out: MetadataConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("allowedRequestHeaders") is not None:
        import capo_bedrock_agentcore_control.types.allowed_request_headers

        out["allowed_request_headers"] = (
            capo_bedrock_agentcore_control.types.allowed_request_headers.deserialize_json(
                data["allowedRequestHeaders"]
            )
        )
    if data.get("allowedQueryParameters") is not None:
        import capo_bedrock_agentcore_control.types.allowed_query_parameters

        out["allowed_query_parameters"] = (
            capo_bedrock_agentcore_control.types.allowed_query_parameters.deserialize_json(
                data["allowedQueryParameters"]
            )
        )
    if data.get("allowedResponseHeaders") is not None:
        import capo_bedrock_agentcore_control.types.allowed_response_headers

        out["allowed_response_headers"] = (
            capo_bedrock_agentcore_control.types.allowed_response_headers.deserialize_json(
                data["allowedResponseHeaders"]
            )
        )
    return out
