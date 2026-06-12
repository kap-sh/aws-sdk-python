"""Generated from Smithy shape ``com.amazonaws.apigateway#GetSdkRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.map_of_string_to_string
    import aws_sdk_api_gateway.types.string


class GetSdkRequest(TypedDict):
    rest_api_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    stage_name: "aws_sdk_api_gateway.types.string.String"
    """<p>The name of the Stage that the SDK will use.</p>"""
    sdk_type: "aws_sdk_api_gateway.types.string.String"
    """<p>The language for the generated SDK. Currently <code>java</code>, <code>javascript</code>, <code>android</code>, <code>objectivec</code> (for iOS), <code>swift</code> (for iOS), and <code>ruby</code> are supported.</p>"""
    parameters: NotRequired[
        "aws_sdk_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>A string-to-string key-value map of query parameters <code>sdkType</code>-dependent properties of the SDK. For <code>sdkType</code> of <code>objectivec</code> or <code>swift</code>, a parameter named <code>classPrefix</code> is required. For <code>sdkType</code> of <code>android</code>, parameters named <code>groupId</code>, <code>artifactId</code>, <code>artifactVersion</code>, and <code>invokerPackage</code> are required. For <code>sdkType</code> of <code>java</code>, parameters named <code>serviceName</code> and <code>javaPackageName</code> are required. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSdkRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSdkRequest:
    out: GetSdkRequest = {}  # type: ignore[typeddict-item]
    return out
