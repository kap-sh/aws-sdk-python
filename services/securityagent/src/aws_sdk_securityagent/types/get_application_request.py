"""Generated from Smithy shape ``com.amazonaws.securityagent#GetApplicationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.application_id


class GetApplicationRequest(TypedDict):
    application_id: "aws_sdk_securityagent.types.application_id.ApplicationId"
    """<p>The unique identifier of the application to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApplicationRequest) -> dict:
    out: dict = {}
    out["applicationId"] = value["application_id"]
    return out


def deserialize_json(data: dict) -> GetApplicationRequest:
    out: GetApplicationRequest = {}  # type: ignore[typeddict-item]
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    else:
        raise DeserializationError("GetApplicationRequest.application_id required")
    return out
