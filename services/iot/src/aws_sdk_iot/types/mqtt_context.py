"""Generated from Smithy shape ``com.amazonaws.iot#MqttContext``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.mqtt_client_id
    import aws_sdk_iot.types.mqtt_password
    import aws_sdk_iot.types.mqtt_username


class MqttContext(TypedDict):
    username: NotRequired["aws_sdk_iot.types.mqtt_username.MqttUsername"]
    """<p>The value of the <code>username</code> key in an MQTT authorization request.</p>"""
    password: NotRequired["aws_sdk_iot.types.mqtt_password.MqttPassword"]
    """<p>The value of the <code>password</code> key in an MQTT authorization request.</p>"""
    client_id: NotRequired["aws_sdk_iot.types.mqtt_client_id.MqttClientId"]
    """<p>The value of the <code>clientId</code> key in an MQTT authorization request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MqttContext) -> dict:
    out: dict = {}
    if "username" in value:
        out["username"] = value["username"]
    if "password" in value:
        import aws_sdk_iot.types.mqtt_password

        out["password"] = aws_sdk_iot.types.mqtt_password.serialize_json(
            value["password"]
        )
    if "client_id" in value:
        out["clientId"] = value["client_id"]
    return out


def deserialize_json(data: dict) -> MqttContext:
    out: MqttContext = {}  # type: ignore[typeddict-item]
    if "username" in data:
        out["username"] = data["username"]
    if "password" in data:
        import aws_sdk_iot.types.mqtt_password

        out["password"] = aws_sdk_iot.types.mqtt_password.deserialize_json(
            data["password"]
        )
    if "clientId" in data:
        out["client_id"] = data["clientId"]
    return out
