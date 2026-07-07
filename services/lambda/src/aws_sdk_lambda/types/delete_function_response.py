"""Generated from Smithy shape ``com.amazonaws.lambda#DeleteFunctionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.integer


class DeleteFunctionResponse(TypedDict, closed=True):
    status_code: "aws_sdk_lambda.types.integer.Integer"
    """<p>The HTTP status code returned by the operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFunctionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFunctionResponse:
    out: DeleteFunctionResponse = {}  # type: ignore[typeddict-item]
    return out
