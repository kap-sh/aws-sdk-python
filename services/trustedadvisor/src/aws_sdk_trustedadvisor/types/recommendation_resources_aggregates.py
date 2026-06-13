"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#RecommendationResourcesAggregates``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_trustedadvisor.errors import DeserializationError


class RecommendationResourcesAggregates(TypedDict):
    ok_count: "int"
    """<p>The number of AWS resources that were flagged to be OK according to the Trusted Advisor check</p>"""
    warning_count: "int"
    """<p>The number of AWS resources that were flagged to have warning according to the Trusted Advisor check </p>"""
    error_count: "int"
    """<p>The number of AWS resources that were flagged to have errors according to the Trusted Advisor check</p>"""
    excluded_count: NotRequired["int"]
    """<p>The number of AWS resources belonging to this Trusted Advisor check that were excluded by the customer</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationResourcesAggregates) -> dict:
    out: dict = {}
    out["okCount"] = value["ok_count"]
    out["warningCount"] = value["warning_count"]
    out["errorCount"] = value["error_count"]
    if "excluded_count" in value:
        out["excludedCount"] = value["excluded_count"]
    return out


def deserialize_json(data: dict) -> RecommendationResourcesAggregates:
    out: RecommendationResourcesAggregates = {}  # type: ignore[typeddict-item]
    if "okCount" in data:
        out["ok_count"] = data["okCount"]
    else:
        raise DeserializationError(
            "RecommendationResourcesAggregates.ok_count required"
        )
    if "warningCount" in data:
        out["warning_count"] = data["warningCount"]
    else:
        raise DeserializationError(
            "RecommendationResourcesAggregates.warning_count required"
        )
    if "errorCount" in data:
        out["error_count"] = data["errorCount"]
    else:
        raise DeserializationError(
            "RecommendationResourcesAggregates.error_count required"
        )
    if "excludedCount" in data:
        out["excluded_count"] = data["excludedCount"]
    return out
