"""Generated from Smithy shape ``com.amazonaws.appconfig#DeleteApplicationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.id


class DeleteApplicationRequest(TypedDict):
    application_id: "aws_sdk_appconfig.types.id.Id"
    """<p>The ID of the application to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteApplicationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteApplicationRequest:
    out: DeleteApplicationRequest = {}  # type: ignore[typeddict-item]
    return out
