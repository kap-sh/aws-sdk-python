"""Generated from Smithy shape ``com.amazonaws.wellarchitected#LensUpgradeSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.lens_alias
    import aws_sdk_wellarchitected.types.lens_arn
    import aws_sdk_wellarchitected.types.lens_version
    import aws_sdk_wellarchitected.types.resource_arn
    import aws_sdk_wellarchitected.types.workload_id
    import aws_sdk_wellarchitected.types.workload_name


class LensUpgradeSummary(TypedDict, closed=True):
    workload_id: NotRequired["aws_sdk_wellarchitected.types.workload_id.WorkloadId"]
    workload_name: NotRequired[
        "aws_sdk_wellarchitected.types.workload_name.WorkloadName"
    ]
    lens_alias: NotRequired["aws_sdk_wellarchitected.types.lens_alias.LensAlias"]
    lens_arn: NotRequired["aws_sdk_wellarchitected.types.lens_arn.LensArn"]
    """<p>The ARN for the lens.</p>"""
    current_lens_version: NotRequired[
        "aws_sdk_wellarchitected.types.lens_version.LensVersion"
    ]
    """<p>The current version of the lens.</p>"""
    latest_lens_version: NotRequired[
        "aws_sdk_wellarchitected.types.lens_version.LensVersion"
    ]
    """<p>The latest version of the lens.</p>"""
    resource_arn: NotRequired["aws_sdk_wellarchitected.types.resource_arn.ResourceArn"]
    """<p> <code>ResourceArn</code> of the lens being upgraded</p>"""
    resource_name: NotRequired[
        "aws_sdk_wellarchitected.types.workload_name.WorkloadName"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: LensUpgradeSummary) -> dict:
    out: dict = {}
    if "workload_id" in value:
        out["WorkloadId"] = value["workload_id"]
    if "workload_name" in value:
        out["WorkloadName"] = value["workload_name"]
    if "lens_alias" in value:
        out["LensAlias"] = value["lens_alias"]
    if "lens_arn" in value:
        out["LensArn"] = value["lens_arn"]
    if "current_lens_version" in value:
        out["CurrentLensVersion"] = value["current_lens_version"]
    if "latest_lens_version" in value:
        out["LatestLensVersion"] = value["latest_lens_version"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "resource_name" in value:
        out["ResourceName"] = value["resource_name"]
    return out


def deserialize_json(data: dict) -> LensUpgradeSummary:
    out: LensUpgradeSummary = {}  # type: ignore[typeddict-item]
    if "WorkloadId" in data:
        out["workload_id"] = data["WorkloadId"]
    if "WorkloadName" in data:
        out["workload_name"] = data["WorkloadName"]
    if "LensAlias" in data:
        out["lens_alias"] = data["LensAlias"]
    if "LensArn" in data:
        out["lens_arn"] = data["LensArn"]
    if "CurrentLensVersion" in data:
        out["current_lens_version"] = data["CurrentLensVersion"]
    if "LatestLensVersion" in data:
        out["latest_lens_version"] = data["LatestLensVersion"]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "ResourceName" in data:
        out["resource_name"] = data["ResourceName"]
    return out
