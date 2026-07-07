"""Generated from Smithy shape ``com.amazonaws.codecommit#ListRepositoriesForApprovalRuleTemplateOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.next_token
    import aws_sdk_codecommit.types.repository_name_list


class ListRepositoriesForApprovalRuleTemplateOutput(TypedDict, closed=True):
    repository_names: NotRequired[
        "aws_sdk_codecommit.types.repository_name_list.RepositoryNameList"
    ]
    """<p>A list of repository names that are associated with the specified approval rule template.</p>"""
    next_token: NotRequired["aws_sdk_codecommit.types.next_token.NextToken"]
    """<p>An enumeration token that allows the operation to batch the next results of the operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListRepositoriesForApprovalRuleTemplateOutput,
) -> dict:
    out: dict = {}
    if "repository_names" in value:
        import aws_sdk_codecommit.types.repository_name_list

        out["repositoryNames"] = (
            aws_sdk_codecommit.types.repository_name_list.serialize_aws_json_1_1(
                value["repository_names"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListRepositoriesForApprovalRuleTemplateOutput:
    out: ListRepositoriesForApprovalRuleTemplateOutput = {}  # type: ignore[typeddict-item]
    if "repositoryNames" in data:
        import aws_sdk_codecommit.types.repository_name_list

        out["repository_names"] = (
            aws_sdk_codecommit.types.repository_name_list.deserialize_aws_json_1_1(
                data["repositoryNames"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
