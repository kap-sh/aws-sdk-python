"""Generated from Smithy shape ``com.amazonaws.glacier#DataRetrievalRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glacier.types.nullable_long
    import capo_glacier.types.string


class DataRetrievalRule(TypedDict, closed=True):
    strategy: NotRequired["capo_glacier.types.string.string"]
    """<p>The type of data retrieval policy to set.</p> <p>Valid values: BytesPerHour|FreeTier|None</p>"""
    bytes_per_hour: NotRequired["capo_glacier.types.nullable_long.NullableLong"]
    """<p>The maximum number of bytes that can be retrieved in an hour.</p> <p>This field is required only if the value of the Strategy field is <code>BytesPerHour</code>. Your PUT operation will be rejected if the Strategy field is not set to <code>BytesPerHour</code> and you set this field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataRetrievalRule) -> dict:
    out: dict = {}
    if "strategy" in value:
        out["Strategy"] = value["strategy"]
    if "bytes_per_hour" in value:
        out["BytesPerHour"] = value["bytes_per_hour"]
    return out


def deserialize_json(data: dict) -> DataRetrievalRule:
    out: DataRetrievalRule = {}  # type: ignore[typeddict-item]
    if "Strategy" in data:
        out["strategy"] = data["Strategy"]
    if "BytesPerHour" in data:
        out["bytes_per_hour"] = data["BytesPerHour"]
    return out
