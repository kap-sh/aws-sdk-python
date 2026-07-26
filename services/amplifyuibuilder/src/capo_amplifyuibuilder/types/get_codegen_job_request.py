"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#GetCodegenJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.app_id
    import capo_amplifyuibuilder.types.uuid


class GetCodegenJobRequest(TypedDict, closed=True):
    app_id: "capo_amplifyuibuilder.types.app_id.AppId"
    """<p>The unique ID of the Amplify app associated with the code generation job.</p>"""
    environment_name: "str"
    """<p>The name of the backend environment that is a part of the Amplify app associated with the code generation job.</p>"""
    id: "capo_amplifyuibuilder.types.uuid.Uuid"
    """<p>The unique ID of the code generation job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCodegenJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCodegenJobRequest:
    out: GetCodegenJobRequest = {}  # type: ignore[typeddict-item]
    return out
