"""Generated from Smithy shape ``com.amazonaws.entityresolution#StartMatchingJobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.entity_name


class StartMatchingJobInput(TypedDict, closed=True):
    workflow_name: "capo_entityresolution.types.entity_name.EntityName"
    """<p>The name of the matching job to be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartMatchingJobInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StartMatchingJobInput:
    out: StartMatchingJobInput = {}  # type: ignore[typeddict-item]
    return out
