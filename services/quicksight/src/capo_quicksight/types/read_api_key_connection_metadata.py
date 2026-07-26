"""Generated from Smithy shape ``com.amazonaws.quicksight#ReadAPIKeyConnectionMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.email
    import capo_quicksight.types.endpoint


class ReadAPIKeyConnectionMetadata(TypedDict, closed=True):
    base_endpoint: "capo_quicksight.types.endpoint.Endpoint"
    """<p>The base endpoint URL for API key authentication.</p>"""
    email: NotRequired["capo_quicksight.types.email.Email"]
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
