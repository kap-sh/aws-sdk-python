"""Generated from Smithy shape ``com.amazonaws.amplify#GetBackendEnvironmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplify.types.app_id
    import aws_sdk_amplify.types.environment_name


class GetBackendEnvironmentRequest(TypedDict, closed=True):
    app_id: "aws_sdk_amplify.types.app_id.AppId"
    """<p>The unique id for an Amplify app. </p>"""
    environment_name: "aws_sdk_amplify.types.environment_name.EnvironmentName"
    """<p>The name for the backend environment. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBackendEnvironmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBackendEnvironmentRequest:
    out: GetBackendEnvironmentRequest = {}  # type: ignore[typeddict-item]
    return out
