"""Generated from Smithy shape ``com.amazonaws.neptunedata#StatisticsSummary``."""

from typing import TypedDict

from typing_extensions import NotRequired


class StatisticsSummary(TypedDict):
    signature_count: NotRequired["int"]
    """<p>The total number of signatures across all characteristic sets.</p>"""
    instance_count: NotRequired["int"]
    """<p>The total number of characteristic-set instances.</p>"""
    predicate_count: NotRequired["int"]
    """<p>The total number of unique predicates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StatisticsSummary) -> dict:
    out: dict = {}
    if "signature_count" in value:
        out["signatureCount"] = value["signature_count"]
    if "instance_count" in value:
        out["instanceCount"] = value["instance_count"]
    if "predicate_count" in value:
        out["predicateCount"] = value["predicate_count"]
    return out


def deserialize_json(data: dict) -> StatisticsSummary:
    out: StatisticsSummary = {}  # type: ignore[typeddict-item]
    if "signatureCount" in data:
        out["signature_count"] = data["signatureCount"]
    if "instanceCount" in data:
        out["instance_count"] = data["instanceCount"]
    if "predicateCount" in data:
        out["predicate_count"] = data["predicateCount"]
    return out
