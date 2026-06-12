"""Generated from Smithy shape ``com.amazonaws.appconfig#GetEnvironmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.id


class GetEnvironmentRequest(TypedDict):
    application_id: "aws_sdk_appconfig.types.id.Id"
    """<p>The ID of the application that includes the environment you want to get.</p>"""
    environment_id: "aws_sdk_appconfig.types.id.Id"
    """<p>The ID of the environment that you want to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEnvironmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEnvironmentRequest:
    out: GetEnvironmentRequest = {}  # type: ignore[typeddict-item]
    return out
