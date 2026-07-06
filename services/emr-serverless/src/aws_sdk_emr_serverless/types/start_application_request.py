"""Generated from Smithy shape ``com.amazonaws.emrserverless#StartApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.application_id


class StartApplicationRequest(TypedDict, closed=True):
    application_id: "aws_sdk_emr_serverless.types.application_id.ApplicationId"
    """<p>The ID of the application to start.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartApplicationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StartApplicationRequest:
    out: StartApplicationRequest = {}  # type: ignore[typeddict-item]
    return out
