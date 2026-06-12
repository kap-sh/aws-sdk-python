"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeAssociationExecutionTargetsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.association_execution_targets_list
    import aws_sdk_ssm.types.next_token


class DescribeAssociationExecutionTargetsResult(TypedDict):
    association_execution_targets: NotRequired[
        "aws_sdk_ssm.types.association_execution_targets_list.AssociationExecutionTargetsList"
    ]
    """<p>Information about the execution.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. Use this token to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAssociationExecutionTargetsResult) -> dict:
    out: dict = {}
    if "association_execution_targets" in value:
        import aws_sdk_ssm.types.association_execution_targets_list

        out["AssociationExecutionTargets"] = (
            aws_sdk_ssm.types.association_execution_targets_list.serialize_aws_json_1_1(
                value["association_execution_targets"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAssociationExecutionTargetsResult:
    out: DescribeAssociationExecutionTargetsResult = {}  # type: ignore[typeddict-item]
    if "AssociationExecutionTargets" in data:
        import aws_sdk_ssm.types.association_execution_targets_list

        out["association_execution_targets"] = (
            aws_sdk_ssm.types.association_execution_targets_list.deserialize_aws_json_1_1(
                data["AssociationExecutionTargets"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
