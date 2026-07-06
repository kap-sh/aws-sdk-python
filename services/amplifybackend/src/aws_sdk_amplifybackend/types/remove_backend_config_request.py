"""Generated from Smithy shape ``com.amazonaws.amplifybackend#RemoveBackendConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.__string


class RemoveBackendConfigRequest(TypedDict, closed=True):
    app_id: "aws_sdk_amplifybackend.types.__string.__string"
    """<p>The app ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveBackendConfigRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RemoveBackendConfigRequest:
    out: RemoveBackendConfigRequest = {}  # type: ignore[typeddict-item]
    return out
