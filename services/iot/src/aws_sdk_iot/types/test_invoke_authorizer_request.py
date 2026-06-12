"""Generated from Smithy shape ``com.amazonaws.iot#TestInvokeAuthorizerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.authorizer_name
    import aws_sdk_iot.types.http_context
    import aws_sdk_iot.types.mqtt_context
    import aws_sdk_iot.types.tls_context
    import aws_sdk_iot.types.token
    import aws_sdk_iot.types.token_signature


class TestInvokeAuthorizerRequest(TypedDict):
    authorizer_name: "aws_sdk_iot.types.authorizer_name.AuthorizerName"
    """<p>The custom authorizer name.</p>"""
    token: NotRequired["aws_sdk_iot.types.token.Token"]
    """<p>The token returned by your custom authentication service.</p>"""
    token_signature: NotRequired["aws_sdk_iot.types.token_signature.TokenSignature"]
    """<p>The signature made with the token and your custom authentication service's private key. This value must be Base-64-encoded.</p>"""
    http_context: NotRequired["aws_sdk_iot.types.http_context.HttpContext"]
    """<p>Specifies a test HTTP authorization request.</p>"""
    mqtt_context: NotRequired["aws_sdk_iot.types.mqtt_context.MqttContext"]
    """<p>Specifies a test MQTT authorization request.</p>"""
    tls_context: NotRequired["aws_sdk_iot.types.tls_context.TlsContext"]
    """<p>Specifies a test TLS authorization request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestInvokeAuthorizerRequest) -> dict:
    out: dict = {}
    if "token" in value:
        out["token"] = value["token"]
    if "token_signature" in value:
        out["tokenSignature"] = value["token_signature"]
    if "http_context" in value:
        import aws_sdk_iot.types.http_context

        out["httpContext"] = aws_sdk_iot.types.http_context.serialize_json(
            value["http_context"]
        )
    if "mqtt_context" in value:
        import aws_sdk_iot.types.mqtt_context

        out["mqttContext"] = aws_sdk_iot.types.mqtt_context.serialize_json(
            value["mqtt_context"]
        )
    if "tls_context" in value:
        import aws_sdk_iot.types.tls_context

        out["tlsContext"] = aws_sdk_iot.types.tls_context.serialize_json(
            value["tls_context"]
        )
    return out


def deserialize_json(data: dict) -> TestInvokeAuthorizerRequest:
    out: TestInvokeAuthorizerRequest = {}  # type: ignore[typeddict-item]
    if "token" in data:
        out["token"] = data["token"]
    if "tokenSignature" in data:
        out["token_signature"] = data["tokenSignature"]
    if "httpContext" in data:
        import aws_sdk_iot.types.http_context

        out["http_context"] = aws_sdk_iot.types.http_context.deserialize_json(
            data["httpContext"]
        )
    if "mqttContext" in data:
        import aws_sdk_iot.types.mqtt_context

        out["mqtt_context"] = aws_sdk_iot.types.mqtt_context.deserialize_json(
            data["mqttContext"]
        )
    if "tlsContext" in data:
        import aws_sdk_iot.types.tls_context

        out["tls_context"] = aws_sdk_iot.types.tls_context.deserialize_json(
            data["tlsContext"]
        )
    return out
