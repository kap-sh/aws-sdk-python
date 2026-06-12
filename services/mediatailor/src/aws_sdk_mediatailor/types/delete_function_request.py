"""Generated from Smithy shape ``com.amazonaws.mediatailor#DeleteFunctionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__string


class DeleteFunctionRequest(TypedDict):
    function_id: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The identifier of the function to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFunctionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFunctionRequest:
    out: DeleteFunctionRequest = {}  # type: ignore[typeddict-item]
    return out
