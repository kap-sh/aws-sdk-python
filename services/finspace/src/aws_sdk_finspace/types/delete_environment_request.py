"""Generated from Smithy shape ``com.amazonaws.finspace#DeleteEnvironmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace.types.id_type


class DeleteEnvironmentRequest(TypedDict, closed=True):
    environment_id: "aws_sdk_finspace.types.id_type.IdType"
    """<p>The identifier for the FinSpace environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEnvironmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEnvironmentRequest:
    out: DeleteEnvironmentRequest = {}  # type: ignore[typeddict-item]
    return out
