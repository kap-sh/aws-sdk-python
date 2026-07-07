"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#GetComponentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.uuid


class GetComponentRequest(TypedDict, closed=True):
    app_id: "str"
    """<p>The unique ID of the Amplify app.</p>"""
    environment_name: "str"
    """<p>The name of the backend environment that is part of the Amplify app.</p>"""
    id: "aws_sdk_amplifyuibuilder.types.uuid.Uuid"
    """<p>The unique ID of the component.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetComponentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetComponentRequest:
    out: GetComponentRequest = {}  # type: ignore[typeddict-item]
    return out
