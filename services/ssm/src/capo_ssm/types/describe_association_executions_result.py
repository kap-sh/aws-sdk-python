"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeAssociationExecutionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.association_executions_list
    import capo_ssm.types.next_token


class DescribeAssociationExecutionsResult(TypedDict, closed=True):
    association_executions: NotRequired[
        "capo_ssm.types.association_executions_list.AssociationExecutionsList"
    ]
    """<p>A list of the executions for the specified association ID.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. Use this token to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAssociationExecutionsResult) -> dict:
    out: dict = {}
    if "association_executions" in value:
        import capo_ssm.types.association_executions_list

        out["AssociationExecutions"] = (
            capo_ssm.types.association_executions_list.serialize_aws_json_1_1(
                value["association_executions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAssociationExecutionsResult:
    out: DescribeAssociationExecutionsResult = {}  # type: ignore[typeddict-item]
    if data.get("AssociationExecutions") is not None:
        import capo_ssm.types.association_executions_list

        out["association_executions"] = (
            capo_ssm.types.association_executions_list.deserialize_aws_json_1_1(
                data["AssociationExecutions"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
