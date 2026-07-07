"""Generated from Smithy shape ``com.amazonaws.appsync#GetApiRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.string


class GetApiRequest(TypedDict, closed=True):
    api_id: "aws_sdk_appsync.types.string.String"
    """<p>The <code>Api</code> ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApiRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetApiRequest:
    out: GetApiRequest = {}  # type: ignore[typeddict-item]
    return out
