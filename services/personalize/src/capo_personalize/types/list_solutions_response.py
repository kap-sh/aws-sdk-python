"""Generated from Smithy shape ``com.amazonaws.personalize#ListSolutionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.next_token
    import capo_personalize.types.solutions


class ListSolutionsResponse(TypedDict, closed=True):
    solutions: NotRequired["capo_personalize.types.solutions.Solutions"]
    """<p>A list of the current solutions.</p>"""
    next_token: NotRequired["capo_personalize.types.next_token.NextToken"]
    """<p>A token for getting the next set of solutions (if they exist).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSolutionsResponse) -> dict:
    out: dict = {}
    if "solutions" in value:
        import capo_personalize.types.solutions

        out["solutions"] = capo_personalize.types.solutions.serialize_aws_json_1_1(
            value["solutions"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSolutionsResponse:
    out: ListSolutionsResponse = {}  # type: ignore[typeddict-item]
    if "solutions" in data:
        import capo_personalize.types.solutions

        out["solutions"] = capo_personalize.types.solutions.deserialize_aws_json_1_1(
            data["solutions"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
