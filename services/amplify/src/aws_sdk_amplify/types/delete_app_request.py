"""Generated from Smithy shape ``com.amazonaws.amplify#DeleteAppRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplify.types.app_id


class DeleteAppRequest(TypedDict):
    app_id: "aws_sdk_amplify.types.app_id.AppId"
    """<p>The unique ID for an Amplify app. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAppRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAppRequest:
    out: DeleteAppRequest = {}  # type: ignore[typeddict-item]
    return out
