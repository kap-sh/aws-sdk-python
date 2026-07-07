"""Generated from Smithy shape ``com.amazonaws.appconfig#GetApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.id


class GetApplicationRequest(TypedDict, closed=True):
    application_id: "aws_sdk_appconfig.types.id.Id"
    """<p>The ID of the application you want to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApplicationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetApplicationRequest:
    out: GetApplicationRequest = {}  # type: ignore[typeddict-item]
    return out
