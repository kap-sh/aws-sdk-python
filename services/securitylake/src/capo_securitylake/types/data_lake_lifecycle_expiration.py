"""Generated from Smithy shape ``com.amazonaws.securitylake#DataLakeLifecycleExpiration``."""

from typing_extensions import NotRequired, TypedDict


class DataLakeLifecycleExpiration(TypedDict, closed=True):
    days: NotRequired["int"]
    """<p>Number of days before data expires in the Amazon Security Lake object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeLifecycleExpiration) -> dict:
    out: dict = {}
    if "days" in value:
        out["days"] = value["days"]
    return out


def deserialize_json(data: dict) -> DataLakeLifecycleExpiration:
    out: DataLakeLifecycleExpiration = {}  # type: ignore[typeddict-item]
    if "days" in data:
        out["days"] = data["days"]
    return out
