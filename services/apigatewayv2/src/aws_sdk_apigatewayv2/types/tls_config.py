"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#TlsConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.string_with_length_between1_and512


class TlsConfig(TypedDict):
    server_name_to_verify: NotRequired[
        "aws_sdk_apigatewayv2.types.string_with_length_between1_and512.StringWithLengthBetween1And512"
    ]
    """<p>If you specify a server name, API Gateway uses it to verify the hostname on the integration's certificate. The server name is also included in the TLS handshake to support Server Name Indication (SNI) or virtual hosting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TlsConfig) -> dict:
    out: dict = {}
    if "server_name_to_verify" in value:
        out["serverNameToVerify"] = value["server_name_to_verify"]
    return out


def deserialize_json(data: dict) -> TlsConfig:
    out: TlsConfig = {}  # type: ignore[typeddict-item]
    if "serverNameToVerify" in data:
        out["server_name_to_verify"] = data["serverNameToVerify"]
    return out
