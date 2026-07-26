"""Generated from Smithy shape ``com.amazonaws.m2#DeploymentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_m2.types.deployment_summary

DeploymentList: TypeAlias = list["capo_m2.types.deployment_summary.DeploymentSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentList) -> list:
    import capo_m2.types.deployment_summary

    out: list = []
    for item in value:
        out.append(capo_m2.types.deployment_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DeploymentList:
    import capo_m2.types.deployment_summary

    out: DeploymentList = []
    for item in data:
        out.append(capo_m2.types.deployment_summary.deserialize_json(item))
    return out
