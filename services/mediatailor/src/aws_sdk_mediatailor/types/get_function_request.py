"""Generated from Smithy shape ``com.amazonaws.mediatailor#GetFunctionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__string


class GetFunctionRequest(TypedDict):
    function_id: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The identifier of the function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFunctionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFunctionRequest:
    out: GetFunctionRequest = {}  # type: ignore[typeddict-item]
    return out
