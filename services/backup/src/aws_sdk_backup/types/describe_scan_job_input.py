"""Generated from Smithy shape ``com.amazonaws.backup#DescribeScanJobInput``."""

from typing_extensions import TypedDict


class DescribeScanJobInput(TypedDict, closed=True):
    scan_job_id: "str"
    """<p>Uniquely identifies a request to Backup to scan a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeScanJobInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeScanJobInput:
    out: DescribeScanJobInput = {}  # type: ignore[typeddict-item]
    return out
