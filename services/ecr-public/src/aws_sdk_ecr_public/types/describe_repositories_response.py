"""Generated from Smithy shape ``com.amazonaws.ecrpublic#DescribeRepositoriesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecr_public.types.next_token
    import aws_sdk_ecr_public.types.repository_list


class DescribeRepositoriesResponse(TypedDict):
    repositories: NotRequired["aws_sdk_ecr_public.types.repository_list.RepositoryList"]
    """<p>A list of repository objects corresponding to valid repositories.</p>"""
    next_token: NotRequired["aws_sdk_ecr_public.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> value to include in a future <code>DescribeRepositories</code> request. When the results of a <code>DescribeRepositories</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. If there are no more results to return, this value is <code>null</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRepositoriesResponse) -> dict:
    out: dict = {}
    if "repositories" in value:
        import aws_sdk_ecr_public.types.repository_list

        out["repositories"] = (
            aws_sdk_ecr_public.types.repository_list.serialize_aws_json_1_1(
                value["repositories"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRepositoriesResponse:
    out: DescribeRepositoriesResponse = {}  # type: ignore[typeddict-item]
    if "repositories" in data:
        import aws_sdk_ecr_public.types.repository_list

        out["repositories"] = (
            aws_sdk_ecr_public.types.repository_list.deserialize_aws_json_1_1(
                data["repositories"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
