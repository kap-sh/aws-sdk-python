"""Generated from Smithy shape ``com.amazonaws.m2#CreateEnvironmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_m2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.identifier


class CreateEnvironmentResponse(TypedDict, closed=True):
    environment_id: "aws_sdk_m2.types.identifier.Identifier"
    """<p>The unique identifier of the runtime environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEnvironmentResponse) -> dict:
    out: dict = {}
    out["environmentId"] = value["environment_id"]
    return out


def deserialize_json(data: dict) -> CreateEnvironmentResponse:
    out: CreateEnvironmentResponse = {}  # type: ignore[typeddict-item]
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    else:
        raise DeserializationError("CreateEnvironmentResponse.environment_id required")
    return out
