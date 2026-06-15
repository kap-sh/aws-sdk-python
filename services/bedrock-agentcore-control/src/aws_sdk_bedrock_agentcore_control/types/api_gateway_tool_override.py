"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ApiGatewayToolOverride``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.rest_api_method


class ApiGatewayToolOverride(TypedDict):
    name: "str"
    """<p>The name of tool. Identifies the tool in the Model Context Protocol.</p>"""
    description: NotRequired["str"]
    """<p>The description of the tool. Provides information about the purpose and usage of the tool. If not provided, uses the description from the API's OpenAPI specification.</p>"""
    path: "str"
    """<p>Resource path in the REST API (e.g., <code>/pets</code>). Must explicitly match an existing path in the REST API.</p>"""
    method: "aws_sdk_bedrock_agentcore_control.types.rest_api_method.RestApiMethod"
    """<p>The HTTP method to expose for the specified path.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApiGatewayToolOverride) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["path"] = value["path"]
    import aws_sdk_bedrock_agentcore_control.types.rest_api_method

    out["method"] = (
        aws_sdk_bedrock_agentcore_control.types.rest_api_method.serialize_json(
            value["method"]
        )
    )
    return out


def deserialize_json(data: dict) -> ApiGatewayToolOverride:
    out: ApiGatewayToolOverride = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ApiGatewayToolOverride.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "path" in data:
        out["path"] = data["path"]
    else:
        raise DeserializationError("ApiGatewayToolOverride.path required")
    if "method" in data:
        import aws_sdk_bedrock_agentcore_control.types.rest_api_method

        out["method"] = (
            aws_sdk_bedrock_agentcore_control.types.rest_api_method.deserialize_json(
                data["method"]
            )
        )
    else:
        raise DeserializationError("ApiGatewayToolOverride.method required")
    return out
