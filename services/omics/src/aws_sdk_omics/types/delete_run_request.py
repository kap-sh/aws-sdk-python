"""Generated from Smithy shape ``com.amazonaws.omics#DeleteRunRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.run_id


class DeleteRunRequest(TypedDict):
    id: "aws_sdk_omics.types.run_id.RunId"
    """<p>The run's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRunRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRunRequest:
    out: DeleteRunRequest = {}  # type: ignore[typeddict-item]
    return out
