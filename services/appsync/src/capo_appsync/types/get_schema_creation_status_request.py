"""Generated from Smithy shape ``com.amazonaws.appsync#GetSchemaCreationStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.string


class GetSchemaCreationStatusRequest(TypedDict, closed=True):
    api_id: "capo_appsync.types.string.String"
    """<p>The API ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSchemaCreationStatusRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSchemaCreationStatusRequest:
    out: GetSchemaCreationStatusRequest = {}  # type: ignore[typeddict-item]
    return out
