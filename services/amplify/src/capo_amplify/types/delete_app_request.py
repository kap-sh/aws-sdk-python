"""Generated from Smithy shape ``com.amazonaws.amplify#DeleteAppRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_amplify.types.app_id


class DeleteAppRequest(TypedDict, closed=True):
    app_id: "capo_amplify.types.app_id.AppId"
    """<p>The unique ID for an Amplify app. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAppRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAppRequest:
    out: DeleteAppRequest = {}  # type: ignore[typeddict-item]
    return out
