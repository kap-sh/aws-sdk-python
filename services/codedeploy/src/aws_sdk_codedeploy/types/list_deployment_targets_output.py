"""Generated from Smithy shape ``com.amazonaws.codedeploy#ListDeploymentTargetsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.next_token
    import aws_sdk_codedeploy.types.target_id_list


class ListDeploymentTargetsOutput(TypedDict):
    target_ids: NotRequired["aws_sdk_codedeploy.types.target_id_list.TargetIdList"]
    """<p> The unique IDs of deployment targets. </p>"""
    next_token: NotRequired["aws_sdk_codedeploy.types.next_token.NextToken"]
    """<p> If a large amount of information is returned, a token identifier is also returned. It can be used in a subsequent <code>ListDeploymentTargets</code> call to return the next set of deployment targets in the list. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDeploymentTargetsOutput) -> dict:
    out: dict = {}
    if "target_ids" in value:
        import aws_sdk_codedeploy.types.target_id_list

        out["targetIds"] = (
            aws_sdk_codedeploy.types.target_id_list.serialize_aws_json_1_1(
                value["target_ids"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDeploymentTargetsOutput:
    out: ListDeploymentTargetsOutput = {}  # type: ignore[typeddict-item]
    if "targetIds" in data:
        import aws_sdk_codedeploy.types.target_id_list

        out["target_ids"] = (
            aws_sdk_codedeploy.types.target_id_list.deserialize_aws_json_1_1(
                data["targetIds"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
