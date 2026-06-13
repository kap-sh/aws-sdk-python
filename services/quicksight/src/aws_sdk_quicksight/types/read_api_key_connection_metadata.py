"""Generated from Smithy shape ``com.amazonaws.quicksight#ReadAPIKeyConnectionMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.email
    import aws_sdk_quicksight.types.endpoint


class ReadAPIKeyConnectionMetadata(TypedDict):
    base_endpoint: "aws_sdk_quicksight.types.endpoint.Endpoint"
    """<p>The base endpoint URL for API key authentication.</p>"""
    email: NotRequired["aws_sdk_quicksight.types.email.Email"]
    """<p>The email address associated with the API key authentication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadAPIKeyConnectionMetadata) -> dict:
    out: dict = {}
    out["BaseEndpoint"] = value["base_endpoint"]
    if "email" in value:
        out["Email"] = value["email"]
    return out


def deserialize_json(data: dict) -> ReadAPIKeyConnectionMetadata:
    out: ReadAPIKeyConnectionMetadata = {}  # type: ignore[typeddict-item]
    if "BaseEndpoint" in data:
        out["base_endpoint"] = data["BaseEndpoint"]
    else:
        raise DeserializationError(
            "ReadAPIKeyConnectionMetadata.base_endpoint required"
        )
    if "Email" in data:
        out["email"] = data["Email"]
    return out
