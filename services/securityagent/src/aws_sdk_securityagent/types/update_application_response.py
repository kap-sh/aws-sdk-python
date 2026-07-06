"""Generated from Smithy shape ``com.amazonaws.securityagent#UpdateApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.application_id


class UpdateApplicationResponse(TypedDict, closed=True):
    application_id: "aws_sdk_securityagent.types.application_id.ApplicationId"
    """<p>The unique identifier of the updated application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApplicationResponse) -> dict:
    out: dict = {}
    out["applicationId"] = value["application_id"]
    return out


def deserialize_json(data: dict) -> UpdateApplicationResponse:
    out: UpdateApplicationResponse = {}  # type: ignore[typeddict-item]
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    else:
        raise DeserializationError("UpdateApplicationResponse.application_id required")
    return out
