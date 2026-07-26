"""Generated from Smithy shape ``com.amazonaws.omics#CancelRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_omics.types.run_id


class CancelRunRequest(TypedDict, closed=True):
    id: "capo_omics.types.run_id.RunId"
    """<p>The run's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelRunRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelRunRequest:
    out: CancelRunRequest = {}  # type: ignore[typeddict-item]
    return out
