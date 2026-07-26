"""Generated from Smithy shape ``com.amazonaws.wellarchitected#UpgradeProfileVersionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.client_request_token
    import capo_wellarchitected.types.milestone_name
    import capo_wellarchitected.types.profile_arn
    import capo_wellarchitected.types.workload_id


class UpgradeProfileVersionInput(TypedDict, closed=True):
    workload_id: "capo_wellarchitected.types.workload_id.WorkloadId"
    profile_arn: "capo_wellarchitected.types.profile_arn.ProfileArn"
    """<p>The profile ARN.</p>"""
    milestone_name: NotRequired[
        "capo_wellarchitected.types.milestone_name.MilestoneName"
    ]
    client_request_token: NotRequired[
        "capo_wellarchitected.types.client_request_token.ClientRequestToken"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpgradeProfileVersionInput) -> dict:
    out: dict = {}
    if "milestone_name" in value:
        out["MilestoneName"] = value["milestone_name"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> UpgradeProfileVersionInput:
    out: UpgradeProfileVersionInput = {}  # type: ignore[typeddict-item]
    if "MilestoneName" in data:
        out["milestone_name"] = data["MilestoneName"]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    return out
