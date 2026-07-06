"""Generated from Smithy shape ``com.amazonaws.codeconnections#ListRepositoryLinksOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codeconnections.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeconnections.types.repository_link_list
    import aws_sdk_codeconnections.types.sharp_next_token


class ListRepositoryLinksOutput(TypedDict, closed=True):
    repository_links: (
        "aws_sdk_codeconnections.types.repository_link_list.RepositoryLinkList"
    )
    """<p>Lists the repository links called by the list repository links operation.</p>"""
    next_token: NotRequired[
        "aws_sdk_codeconnections.types.sharp_next_token.SharpNextToken"
    ]
    """<p>An enumeration token that allows the operation to batch the results of the operation. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRepositoryLinksOutput) -> dict:
    out: dict = {}
    import aws_sdk_codeconnections.types.repository_link_list

    out["RepositoryLinks"] = (
        aws_sdk_codeconnections.types.repository_link_list.serialize_aws_json_1_0(
            value["repository_links"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRepositoryLinksOutput:
    out: ListRepositoryLinksOutput = {}  # type: ignore[typeddict-item]
    if "RepositoryLinks" in data:
        import aws_sdk_codeconnections.types.repository_link_list

        out["repository_links"] = (
            aws_sdk_codeconnections.types.repository_link_list.deserialize_aws_json_1_0(
                data["RepositoryLinks"]
            )
        )
    else:
        raise DeserializationError(
            "ListRepositoryLinksOutput.repository_links required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
