"""Generated from Smithy shape ``com.amazonaws.amplify#ProductionBranch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplify.types.branch_name
    import aws_sdk_amplify.types.last_deploy_time
    import aws_sdk_amplify.types.status
    import aws_sdk_amplify.types.thumbnail_url


class ProductionBranch(TypedDict, closed=True):
    last_deploy_time: NotRequired[
        "aws_sdk_amplify.types.last_deploy_time.LastDeployTime"
    ]
    """<p>The last deploy time of the production branch. </p>"""
    status: NotRequired["aws_sdk_amplify.types.status.Status"]
    """<p>The status of the production branch. </p>"""
    thumbnail_url: NotRequired["aws_sdk_amplify.types.thumbnail_url.ThumbnailUrl"]
    """<p>The thumbnail URL for the production branch. </p>"""
    branch_name: NotRequired["aws_sdk_amplify.types.branch_name.BranchName"]
    """<p>The branch name for the production branch. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProductionBranch) -> dict:
    out: dict = {}
    if "last_deploy_time" in value:
        import aws_sdk_amplify.types.last_deploy_time

        out["lastDeployTime"] = aws_sdk_amplify.types.last_deploy_time.serialize_json(
            value["last_deploy_time"]
        )
    if "status" in value:
        out["status"] = value["status"]
    if "thumbnail_url" in value:
        out["thumbnailUrl"] = value["thumbnail_url"]
    if "branch_name" in value:
        out["branchName"] = value["branch_name"]
    return out


def deserialize_json(data: dict) -> ProductionBranch:
    out: ProductionBranch = {}  # type: ignore[typeddict-item]
    if "lastDeployTime" in data:
        import aws_sdk_amplify.types.last_deploy_time

        out["last_deploy_time"] = (
            aws_sdk_amplify.types.last_deploy_time.deserialize_json(
                data["lastDeployTime"]
            )
        )
    if "status" in data:
        out["status"] = data["status"]
    if "thumbnailUrl" in data:
        out["thumbnail_url"] = data["thumbnailUrl"]
    if "branchName" in data:
        out["branch_name"] = data["branchName"]
    return out
