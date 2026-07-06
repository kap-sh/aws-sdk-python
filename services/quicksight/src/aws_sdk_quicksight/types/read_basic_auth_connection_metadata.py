"""Generated from Smithy shape ``com.amazonaws.quicksight#ReadBasicAuthConnectionMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.action_user_name
    import aws_sdk_quicksight.types.endpoint


class ReadBasicAuthConnectionMetadata(TypedDict, closed=True):
    base_endpoint: "aws_sdk_quicksight.types.endpoint.Endpoint"
    """<p>The base endpoint URL for basic authentication.</p>"""
    username: "aws_sdk_quicksight.types.action_user_name.ActionUserName"
    """<p>The username used for basic authentication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadBasicAuthConnectionMetadata) -> dict:
    out: dict = {}
    out["BaseEndpoint"] = value["base_endpoint"]
    out["Username"] = value["username"]
    return out


def deserialize_json(data: dict) -> ReadBasicAuthConnectionMetadata:
    out: ReadBasicAuthConnectionMetadata = {}  # type: ignore[typeddict-item]
    if "BaseEndpoint" in data:
        out["base_endpoint"] = data["BaseEndpoint"]
    else:
        raise DeserializationError(
            "ReadBasicAuthConnectionMetadata.base_endpoint required"
        )
    if "Username" in data:
        out["username"] = data["Username"]
    else:
        raise DeserializationError("ReadBasicAuthConnectionMetadata.username required")
    return out
