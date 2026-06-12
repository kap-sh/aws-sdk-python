"""Generated from Smithy shape ``com.amazonaws.appsync#GetSchemaCreationStatusRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.string


class GetSchemaCreationStatusRequest(TypedDict):
    api_id: "aws_sdk_appsync.types.string.String"
    """<p>The API ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSchemaCreationStatusRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSchemaCreationStatusRequest:
    out: GetSchemaCreationStatusRequest = {}  # type: ignore[typeddict-item]
    return out
