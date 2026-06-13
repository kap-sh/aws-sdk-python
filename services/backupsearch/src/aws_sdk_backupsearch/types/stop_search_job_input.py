"""Generated from Smithy shape ``com.amazonaws.backupsearch#StopSearchJobInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backupsearch.types.generic_id


class StopSearchJobInput(TypedDict):
    search_job_identifier: "aws_sdk_backupsearch.types.generic_id.GenericId"
    """<p>The unique string that specifies the search job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopSearchJobInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopSearchJobInput:
    out: StopSearchJobInput = {}  # type: ignore[typeddict-item]
    return out
