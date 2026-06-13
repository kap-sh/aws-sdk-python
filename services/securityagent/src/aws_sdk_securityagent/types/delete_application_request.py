"""Generated from Smithy shape ``com.amazonaws.securityagent#DeleteApplicationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.application_id


class DeleteApplicationRequest(TypedDict):
    application_id: "aws_sdk_securityagent.types.application_id.ApplicationId"
    """<p>The unique identifier of the application to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteApplicationRequest) -> dict:
    out: dict = {}
    out["applicationId"] = value["application_id"]
    return out


def deserialize_json(data: dict) -> DeleteApplicationRequest:
    out: DeleteApplicationRequest = {}  # type: ignore[typeddict-item]
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    else:
        raise DeserializationError("DeleteApplicationRequest.application_id required")
    return out
