"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#DeleteFormRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.uuid


class DeleteFormRequest(TypedDict, closed=True):
    app_id: "str"
    """<p>The unique ID of the Amplify app associated with the form to delete.</p>"""
    environment_name: "str"
    """<p>The name of the backend environment that is a part of the Amplify app.</p>"""
    id: "aws_sdk_amplifyuibuilder.types.uuid.Uuid"
    """<p>The unique ID of the form to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFormRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFormRequest:
    out: DeleteFormRequest = {}  # type: ignore[typeddict-item]
    return out
