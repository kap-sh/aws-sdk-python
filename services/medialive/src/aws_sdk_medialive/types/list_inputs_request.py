"""Generated from Smithy shape ``com.amazonaws.medialive#ListInputsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.max_results


class ListInputsRequest(TypedDict):
    max_results: NotRequired["aws_sdk_medialive.types.max_results.MaxResults"]
    next_token: NotRequired["aws_sdk_medialive.types.__string.__string"]


# --- restJson1 ser/de ---
def serialize_json(value: ListInputsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListInputsRequest:
    out: ListInputsRequest = {}  # type: ignore[typeddict-item]
    return out
