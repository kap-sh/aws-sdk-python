"""Generated from Smithy shape ``com.amazonaws.finspace#GetKxEnvironmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace.types.id_type


class GetKxEnvironmentRequest(TypedDict):
    environment_id: "aws_sdk_finspace.types.id_type.IdType"
    """<p>A unique identifier for the kdb environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetKxEnvironmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetKxEnvironmentRequest:
    out: GetKxEnvironmentRequest = {}  # type: ignore[typeddict-item]
    return out
