"""Generated from Smithy shape ``com.amazonaws.m2#UpdateEnvironmentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_m2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.identifier


class UpdateEnvironmentResponse(TypedDict):
    environment_id: "aws_sdk_m2.types.identifier.Identifier"
    """<p>The unique identifier of the runtime environment that was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEnvironmentResponse) -> dict:
    out: dict = {}
    out["environmentId"] = value["environment_id"]
    return out


def deserialize_json(data: dict) -> UpdateEnvironmentResponse:
    out: UpdateEnvironmentResponse = {}  # type: ignore[typeddict-item]
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    else:
        raise DeserializationError("UpdateEnvironmentResponse.environment_id required")
    return out
