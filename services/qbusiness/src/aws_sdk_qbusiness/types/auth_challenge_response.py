"""Generated from Smithy shape ``com.amazonaws.qbusiness#AuthChallengeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.authorization_response_map


class AuthChallengeResponse(TypedDict, closed=True):
    response_map: (
        "aws_sdk_qbusiness.types.authorization_response_map.AuthorizationResponseMap"
    )
    """<p>The mapping of key-value pairs in an authentication challenge response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthChallengeResponse) -> dict:
    out: dict = {}
    import aws_sdk_qbusiness.types.authorization_response_map

    out["responseMap"] = (
        aws_sdk_qbusiness.types.authorization_response_map.serialize_json(
            value["response_map"]
        )
    )
    return out


def deserialize_json(data: dict) -> AuthChallengeResponse:
    out: AuthChallengeResponse = {}  # type: ignore[typeddict-item]
    if "responseMap" in data:
        import aws_sdk_qbusiness.types.authorization_response_map

        out["response_map"] = (
            aws_sdk_qbusiness.types.authorization_response_map.deserialize_json(
                data["responseMap"]
            )
        )
    else:
        raise DeserializationError("AuthChallengeResponse.response_map required")
    return out
