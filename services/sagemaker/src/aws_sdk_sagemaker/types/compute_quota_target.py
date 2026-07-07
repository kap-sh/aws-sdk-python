"""Generated from Smithy shape ``com.amazonaws.sagemaker#ComputeQuotaTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.compute_quota_target_team_name
    import aws_sdk_sagemaker.types.fair_share_weight


class ComputeQuotaTarget(TypedDict, closed=True):
    team_name: NotRequired[
        "aws_sdk_sagemaker.types.compute_quota_target_team_name.ComputeQuotaTargetTeamName"
    ]
    """<p>Name of the team to allocate compute resources to.</p>"""
    fair_share_weight: NotRequired[
        "aws_sdk_sagemaker.types.fair_share_weight.FairShareWeight"
    ]
    """<p>Assigned entity fair-share weight. Idle compute will be shared across entities based on these assigned weights. This weight is only used when <code>FairShare</code> is enabled.</p> <p>A weight of 0 is the lowest priority and 100 is the highest. Weight 0 is the default.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComputeQuotaTarget) -> dict:
    out: dict = {}
    if "team_name" in value:
        out["TeamName"] = value["team_name"]
    if "fair_share_weight" in value:
        out["FairShareWeight"] = value["fair_share_weight"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ComputeQuotaTarget:
    out: ComputeQuotaTarget = {}  # type: ignore[typeddict-item]
    if "TeamName" in data:
        out["team_name"] = data["TeamName"]
    if "FairShareWeight" in data:
        out["fair_share_weight"] = data["FairShareWeight"]
    return out
