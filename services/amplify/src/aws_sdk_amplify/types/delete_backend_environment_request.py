"""Generated from Smithy shape ``com.amazonaws.amplify#DeleteBackendEnvironmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplify.types.app_id
    import aws_sdk_amplify.types.environment_name


class DeleteBackendEnvironmentRequest(TypedDict, closed=True):
    app_id: "aws_sdk_amplify.types.app_id.AppId"
    """<p>The unique ID of an Amplify app. </p>"""
    environment_name: "aws_sdk_amplify.types.environment_name.EnvironmentName"
    """<p>The name of a backend environment of an Amplify app. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBackendEnvironmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteBackendEnvironmentRequest:
    out: DeleteBackendEnvironmentRequest = {}  # type: ignore[typeddict-item]
    return out
