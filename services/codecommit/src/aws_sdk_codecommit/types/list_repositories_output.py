"""Generated from Smithy shape ``com.amazonaws.codecommit#ListRepositoriesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.next_token
    import aws_sdk_codecommit.types.repository_name_id_pair_list


class ListRepositoriesOutput(TypedDict):
    repositories: NotRequired[
        "aws_sdk_codecommit.types.repository_name_id_pair_list.RepositoryNameIdPairList"
    ]
    """<p>Lists the repositories called by the list repositories operation.</p>"""
    next_token: NotRequired["aws_sdk_codecommit.types.next_token.NextToken"]
    """<p>An enumeration token that allows the operation to batch the results of the operation. Batch sizes are 1,000 for list repository operations. When the client sends the token back to CodeCommit, another page of 1,000 records is retrieved.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRepositoriesOutput) -> dict:
    out: dict = {}
    if "repositories" in value:
        import aws_sdk_codecommit.types.repository_name_id_pair_list

        out["repositories"] = (
            aws_sdk_codecommit.types.repository_name_id_pair_list.serialize_aws_json_1_1(
                value["repositories"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRepositoriesOutput:
    out: ListRepositoriesOutput = {}  # type: ignore[typeddict-item]
    if "repositories" in data:
        import aws_sdk_codecommit.types.repository_name_id_pair_list

        out["repositories"] = (
            aws_sdk_codecommit.types.repository_name_id_pair_list.deserialize_aws_json_1_1(
                data["repositories"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
