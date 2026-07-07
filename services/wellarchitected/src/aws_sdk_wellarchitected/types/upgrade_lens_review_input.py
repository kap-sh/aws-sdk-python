"""Generated from Smithy shape ``com.amazonaws.wellarchitected#UpgradeLensReviewInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.client_request_token
    import aws_sdk_wellarchitected.types.lens_alias
    import aws_sdk_wellarchitected.types.milestone_name
    import aws_sdk_wellarchitected.types.workload_id


class UpgradeLensReviewInput(TypedDict, closed=True):
    workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId"
    lens_alias: "aws_sdk_wellarchitected.types.lens_alias.LensAlias"
    milestone_name: NotRequired[
        "aws_sdk_wellarchitected.types.milestone_name.MilestoneName"
    ]
    client_request_token: NotRequired[
        "aws_sdk_wellarchitected.types.client_request_token.ClientRequestToken"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpgradeLensReviewInput) -> dict:
    out: dict = {}
    if "milestone_name" in value:
        out["MilestoneName"] = value["milestone_name"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> UpgradeLensReviewInput:
    out: UpgradeLensReviewInput = {}  # type: ignore[typeddict-item]
    if "MilestoneName" in data:
        out["milestone_name"] = data["MilestoneName"]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    return out
