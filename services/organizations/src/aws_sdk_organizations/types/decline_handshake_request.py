"""Generated from Smithy shape ``com.amazonaws.organizations#DeclineHandshakeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_organizations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_organizations.types.handshake_id


class DeclineHandshakeRequest(TypedDict):
    handshake_id: "aws_sdk_organizations.types.handshake_id.HandshakeId"
    """<p>ID for the handshake that you want to decline. You can get the ID from the <a>ListHandshakesForAccount</a> operation.</p> <p>The <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a> for handshake ID string requires \"h-\" followed by from 8 to 32 lowercase letters or digits.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeclineHandshakeRequest) -> dict:
    out: dict = {}
    out["HandshakeId"] = value["handshake_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeclineHandshakeRequest:
    out: DeclineHandshakeRequest = {}  # type: ignore[typeddict-item]
    if "HandshakeId" in data:
        out["handshake_id"] = data["HandshakeId"]
    else:
        raise DeserializationError("DeclineHandshakeRequest.handshake_id required")
    return out
