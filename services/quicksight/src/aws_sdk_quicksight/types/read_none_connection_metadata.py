"""Generated from Smithy shape ``com.amazonaws.quicksight#ReadNoneConnectionMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.endpoint


class ReadNoneConnectionMetadata(TypedDict, closed=True):
    base_endpoint: "aws_sdk_quicksight.types.endpoint.Endpoint"
    """<p>The base endpoint URL for connections that do not require authentication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadNoneConnectionMetadata) -> dict:
    out: dict = {}
    out["BaseEndpoint"] = value["base_endpoint"]
    return out


def deserialize_json(data: dict) -> ReadNoneConnectionMetadata:
    out: ReadNoneConnectionMetadata = {}  # type: ignore[typeddict-item]
    if "BaseEndpoint" in data:
        out["base_endpoint"] = data["BaseEndpoint"]
    else:
        raise DeserializationError("ReadNoneConnectionMetadata.base_endpoint required")
    return out
