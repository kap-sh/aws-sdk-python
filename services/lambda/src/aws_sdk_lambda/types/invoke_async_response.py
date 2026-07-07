"""Generated from Smithy shape ``com.amazonaws.lambda#InvokeAsyncResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.http_status


class InvokeAsyncResponse(TypedDict, closed=True):
    status: "aws_sdk_lambda.types.http_status.HttpStatus"
    """<p>The status code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeAsyncResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> InvokeAsyncResponse:
    out: InvokeAsyncResponse = {}  # type: ignore[typeddict-item]
    return out
