"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ExchangeCodeForTokenRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.exchange_code_for_token_request_body
    import aws_sdk_amplifyuibuilder.types.token_providers


class ExchangeCodeForTokenRequest(TypedDict, closed=True):
    provider: "aws_sdk_amplifyuibuilder.types.token_providers.TokenProviders"
    """<p>The third-party provider for the token. The only valid value is <code>figma</code>.</p>"""
    request: "aws_sdk_amplifyuibuilder.types.exchange_code_for_token_request_body.ExchangeCodeForTokenRequestBody"
    """<p>Describes the configuration of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExchangeCodeForTokenRequest) -> dict:
    out: dict = {}
    import aws_sdk_amplifyuibuilder.types.exchange_code_for_token_request_body

    out["request"] = (
        aws_sdk_amplifyuibuilder.types.exchange_code_for_token_request_body.serialize_json(
            value["request"]
        )
    )
    return out


def deserialize_json(data: dict) -> ExchangeCodeForTokenRequest:
    out: ExchangeCodeForTokenRequest = {}  # type: ignore[typeddict-item]
    if "request" in data:
        import aws_sdk_amplifyuibuilder.types.exchange_code_for_token_request_body

        out["request"] = (
            aws_sdk_amplifyuibuilder.types.exchange_code_for_token_request_body.deserialize_json(
                data["request"]
            )
        )
    else:
        raise DeserializationError("ExchangeCodeForTokenRequest.request required")
    return out
