"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ErrorDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.error_message
    import capo_elasticsearch_service.types.error_type


class ErrorDetails(TypedDict, closed=True):
    error_type: NotRequired["capo_elasticsearch_service.types.error_type.ErrorType"]
    error_message: NotRequired[
        "capo_elasticsearch_service.types.error_message.ErrorMessage"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ErrorDetails) -> dict:
    out: dict = {}
    if "error_type" in value:
        out["ErrorType"] = value["error_type"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> ErrorDetails:
    out: ErrorDetails = {}  # type: ignore[typeddict-item]
    if "ErrorType" in data:
        out["error_type"] = data["ErrorType"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
