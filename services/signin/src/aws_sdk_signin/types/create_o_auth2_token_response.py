"""Generated from Smithy shape ``com.amazonaws.signin#CreateOAuth2TokenResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_signin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_signin.types.create_o_auth2_token_response_body


class CreateOAuth2TokenResponse(TypedDict):
    token_output: "aws_sdk_signin.types.create_o_auth2_token_response_body.CreateOAuth2TokenResponseBody"
    """Flattened token operation outputs The specific response fields depend on the grant_type used in the request"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateOAuth2TokenResponse) -> dict:
    out: dict = {}
    import aws_sdk_signin.types.create_o_auth2_token_response_body

    out["tokenOutput"] = (
        aws_sdk_signin.types.create_o_auth2_token_response_body.serialize_json(
            value["token_output"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateOAuth2TokenResponse:
    out: CreateOAuth2TokenResponse = {}  # type: ignore[typeddict-item]
    if "tokenOutput" in data:
        import aws_sdk_signin.types.create_o_auth2_token_response_body

        out["token_output"] = (
            aws_sdk_signin.types.create_o_auth2_token_response_body.deserialize_json(
                data["tokenOutput"]
            )
        )
    else:
        raise DeserializationError("CreateOAuth2TokenResponse.token_output required")
    return out
