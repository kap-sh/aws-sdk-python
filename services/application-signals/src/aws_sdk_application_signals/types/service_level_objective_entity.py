"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceLevelObjectiveEntity``."""

from typing_extensions import NotRequired, TypedDict


class ServiceLevelObjectiveEntity(TypedDict, closed=True):
    slo_name: NotRequired["str"]
    """<p>The name of the service level objective.</p>"""
    slo_arn: NotRequired["str"]
    """<p>The ARN of the service level objective. The SLO must be provided with ARN for cross-account access.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceLevelObjectiveEntity) -> dict:
    out: dict = {}
    if "slo_name" in value:
        out["SloName"] = value["slo_name"]
    if "slo_arn" in value:
        out["SloArn"] = value["slo_arn"]
    return out


def deserialize_json(data: dict) -> ServiceLevelObjectiveEntity:
    out: ServiceLevelObjectiveEntity = {}  # type: ignore[typeddict-item]
    if "SloName" in data:
        out["slo_name"] = data["SloName"]
    if "SloArn" in data:
        out["slo_arn"] = data["SloArn"]
    return out
