"""Generated from Smithy shape ``com.amazonaws.finspace#GetEnvironmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace.types.id_type


class GetEnvironmentRequest(TypedDict):
    environment_id: "aws_sdk_finspace.types.id_type.IdType"
    """<p>The identifier of the FinSpace environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEnvironmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEnvironmentRequest:
    out: GetEnvironmentRequest = {}  # type: ignore[typeddict-item]
    return out
