"""Generated from Smithy shape ``com.amazonaws.proton#ListRepositoriesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.next_token
    import aws_sdk_proton.types.repository_summary_list


class ListRepositoriesOutput(TypedDict):
    next_token: NotRequired["aws_sdk_proton.types.next_token.NextToken"]
    """<p>A token that indicates the location of the next repository in the array of repositories, after the current requested list of repositories. </p>"""
    repositories: "aws_sdk_proton.types.repository_summary_list.RepositorySummaryList"
    """<p>An array of repository links.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRepositoriesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_proton.types.repository_summary_list

    out["repositories"] = (
        aws_sdk_proton.types.repository_summary_list.serialize_aws_json_1_0(
            value["repositories"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRepositoriesOutput:
    out: ListRepositoriesOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "repositories" in data:
        import aws_sdk_proton.types.repository_summary_list

        out["repositories"] = (
            aws_sdk_proton.types.repository_summary_list.deserialize_aws_json_1_0(
                data["repositories"]
            )
        )
    else:
        raise DeserializationError("ListRepositoriesOutput.repositories required")
    return out
