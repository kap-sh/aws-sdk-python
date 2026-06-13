"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#DeleteComponentRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.uuid


class DeleteComponentRequest(TypedDict):
    app_id: "str"
    """<p>The unique ID of the Amplify app associated with the component to delete.</p>"""
    environment_name: "str"
    """<p>The name of the backend environment that is a part of the Amplify app.</p>"""
    id: "aws_sdk_amplifyuibuilder.types.uuid.Uuid"
    """<p>The unique ID of the component to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteComponentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteComponentRequest:
    out: DeleteComponentRequest = {}  # type: ignore[typeddict-item]
    return out
