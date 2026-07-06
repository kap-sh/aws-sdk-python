"""Generated from Smithy shape ``com.amazonaws.medialive#CreatePartnerInputRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.tags


class CreatePartnerInputRequest(TypedDict, closed=True):
    input_id: "aws_sdk_medialive.types.__string.__string"
    """Unique ID of the input."""
    request_id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Unique identifier of the request to ensure the request is handled exactly once in case of retries."""
    tags: NotRequired["aws_sdk_medialive.types.tags.Tags"]
    """A collection of key-value pairs."""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePartnerInputRequest) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "tags" in value:
        import aws_sdk_medialive.types.tags

        out["tags"] = aws_sdk_medialive.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreatePartnerInputRequest:
    out: CreatePartnerInputRequest = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "tags" in data:
        import aws_sdk_medialive.types.tags

        out["tags"] = aws_sdk_medialive.types.tags.deserialize_json(data["tags"])
    return out
