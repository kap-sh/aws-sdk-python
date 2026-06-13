"""Generated from Smithy shape ``com.amazonaws.entityresolution#StartMatchingJobInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.entity_name


class StartMatchingJobInput(TypedDict):
    workflow_name: "aws_sdk_entityresolution.types.entity_name.EntityName"
    """<p>The name of the matching job to be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartMatchingJobInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StartMatchingJobInput:
    out: StartMatchingJobInput = {}  # type: ignore[typeddict-item]
    return out
