"""Generated from Smithy shape ``com.amazonaws.amplifybackend#DeleteBackendRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.__string


class DeleteBackendRequest(TypedDict, closed=True):
    app_id: "aws_sdk_amplifybackend.types.__string.__string"
    """<p>The app ID.</p>"""
    backend_environment_name: "aws_sdk_amplifybackend.types.__string.__string"
    """<p>The name of the backend environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBackendRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteBackendRequest:
    out: DeleteBackendRequest = {}  # type: ignore[typeddict-item]
    return out
