"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#LinkedAccountEmail``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.email


class LinkedAccountEmail(TypedDict):
    email_address: "aws_sdk_bedrock_agentcore.types.email.Email"
    """<p>The email address used for the linked account. Must be a valid email format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LinkedAccountEmail) -> dict:
    out: dict = {}
    out["emailAddress"] = value["email_address"]
    return out


def deserialize_json(data: dict) -> LinkedAccountEmail:
    out: LinkedAccountEmail = {}  # type: ignore[typeddict-item]
    if "emailAddress" in data:
        out["email_address"] = data["emailAddress"]
    else:
        raise DeserializationError("LinkedAccountEmail.email_address required")
    return out
