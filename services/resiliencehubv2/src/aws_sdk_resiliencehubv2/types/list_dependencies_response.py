"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListDependenciesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.dependency_summary_list
    import aws_sdk_resiliencehubv2.types.next_token


class ListDependenciesResponse(TypedDict):
    dependency_summaries: (
        "aws_sdk_resiliencehubv2.types.dependency_summary_list.DependencySummaryList"
    )
    """<p>The list of dependency summaries.</p>"""
    next_token: NotRequired["aws_sdk_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListDependenciesResponse) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehubv2.types.dependency_summary_list

    out["dependencySummaries"] = (
        aws_sdk_resiliencehubv2.types.dependency_summary_list.serialize_json(
            value["dependency_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDependenciesResponse:
    out: ListDependenciesResponse = {}  # type: ignore[typeddict-item]
    if "dependencySummaries" in data:
        import aws_sdk_resiliencehubv2.types.dependency_summary_list

        out["dependency_summaries"] = (
            aws_sdk_resiliencehubv2.types.dependency_summary_list.deserialize_json(
                data["dependencySummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListDependenciesResponse.dependency_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
