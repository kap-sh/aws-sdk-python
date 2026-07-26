"""Generated from Smithy shape ``com.amazonaws.emrserverless#StopApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_emr_serverless.types.application_id


class StopApplicationRequest(TypedDict, closed=True):
    application_id: "capo_emr_serverless.types.application_id.ApplicationId"
    """<p>The ID of the application to stop.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopApplicationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopApplicationRequest:
    out: StopApplicationRequest = {}  # type: ignore[typeddict-item]
    return out
