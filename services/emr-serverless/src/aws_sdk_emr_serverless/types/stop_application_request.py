"""Generated from Smithy shape ``com.amazonaws.emrserverless#StopApplicationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.application_id


class StopApplicationRequest(TypedDict):
    application_id: "aws_sdk_emr_serverless.types.application_id.ApplicationId"
    """<p>The ID of the application to stop.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopApplicationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopApplicationRequest:
    out: StopApplicationRequest = {}  # type: ignore[typeddict-item]
    return out
