"""Generated from Smithy shape ``com.amazonaws.backup#DescribeCopyJobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_backup.types.string


class DescribeCopyJobInput(TypedDict, closed=True):
    copy_job_id: "capo_backup.types.string.string"
    """<p>Uniquely identifies a copy job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeCopyJobInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeCopyJobInput:
    out: DescribeCopyJobInput = {}  # type: ignore[typeddict-item]
    return out
