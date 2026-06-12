"""Generated from Smithy shape ``com.amazonaws.m2#DeleteEnvironmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_m2.types.identifier


class DeleteEnvironmentRequest(TypedDict):
    environment_id: "aws_sdk_m2.types.identifier.Identifier"
    """<p>The unique identifier of the runtime environment you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEnvironmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEnvironmentRequest:
    out: DeleteEnvironmentRequest = {}  # type: ignore[typeddict-item]
    return out
