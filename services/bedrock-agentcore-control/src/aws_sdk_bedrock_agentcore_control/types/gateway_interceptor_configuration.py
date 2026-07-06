"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GatewayInterceptorConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.gateway_interception_points
    import aws_sdk_bedrock_agentcore_control.types.interceptor_configuration
    import aws_sdk_bedrock_agentcore_control.types.interceptor_input_configuration


class GatewayInterceptorConfiguration(TypedDict, closed=True):
    interceptor: "aws_sdk_bedrock_agentcore_control.types.interceptor_configuration.InterceptorConfiguration"
    """<p>The infrastructure settings of an interceptor configuration. This structure defines how the interceptor can be invoked.</p>"""
    interception_points: "aws_sdk_bedrock_agentcore_control.types.gateway_interception_points.GatewayInterceptionPoints"
    """<p>The supported points of interception. This field specifies which points during the gateway invocation to invoke the interceptor</p>"""
    input_configuration: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.interceptor_input_configuration.InterceptorInputConfiguration"
    ]
    """<p>The configuration for the input of the interceptor. This field specifies how the input to the interceptor is constructed</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GatewayInterceptorConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.interceptor_configuration

    out["interceptor"] = (
        aws_sdk_bedrock_agentcore_control.types.interceptor_configuration.serialize_json(
            value["interceptor"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.gateway_interception_points

    out["interceptionPoints"] = (
        aws_sdk_bedrock_agentcore_control.types.gateway_interception_points.serialize_json(
            value["interception_points"]
        )
    )
    if "input_configuration" in value:
        import aws_sdk_bedrock_agentcore_control.types.interceptor_input_configuration

        out["inputConfiguration"] = (
            aws_sdk_bedrock_agentcore_control.types.interceptor_input_configuration.serialize_json(
                value["input_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GatewayInterceptorConfiguration:
    out: GatewayInterceptorConfiguration = {}  # type: ignore[typeddict-item]
    if "interceptor" in data:
        import aws_sdk_bedrock_agentcore_control.types.interceptor_configuration

        out["interceptor"] = (
            aws_sdk_bedrock_agentcore_control.types.interceptor_configuration.deserialize_json(
                data["interceptor"]
            )
        )
    else:
        raise DeserializationError(
            "GatewayInterceptorConfiguration.interceptor required"
        )
    if "interceptionPoints" in data:
        import aws_sdk_bedrock_agentcore_control.types.gateway_interception_points

        out["interception_points"] = (
            aws_sdk_bedrock_agentcore_control.types.gateway_interception_points.deserialize_json(
                data["interceptionPoints"]
            )
        )
    else:
        raise DeserializationError(
            "GatewayInterceptorConfiguration.interception_points required"
        )
    if "inputConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.interceptor_input_configuration

        out["input_configuration"] = (
            aws_sdk_bedrock_agentcore_control.types.interceptor_input_configuration.deserialize_json(
                data["inputConfiguration"]
            )
        )
    return out
