"""Generated from Smithy shape ``com.amazonaws.iot#TermsAggregation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.max_buckets


class TermsAggregation(TypedDict, closed=True):
    max_buckets: NotRequired["capo_iot.types.max_buckets.MaxBuckets"]
    """<p>The number of buckets to return in the response. Default to 10.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TermsAggregation) -> dict:
    out: dict = {}
    if "max_buckets" in value:
        out["maxBuckets"] = value["max_buckets"]
    return out


def deserialize_json(data: dict) -> TermsAggregation:
    out: TermsAggregation = {}  # type: ignore[typeddict-item]
    if "maxBuckets" in data:
        out["max_buckets"] = data["maxBuckets"]
    return out
