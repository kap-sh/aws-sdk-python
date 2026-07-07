"""Generated from Smithy shape ``com.amazonaws.codecommit#ListRepositoriesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.next_token
    import aws_sdk_codecommit.types.order_enum
    import aws_sdk_codecommit.types.sort_by_enum


class ListRepositoriesInput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_codecommit.types.next_token.NextToken"]
    """<p>An enumeration token that allows the operation to batch the results of the operation. Batch sizes are 1,000 for list repository operations. When the client sends the token back to CodeCommit, another page of 1,000 records is retrieved.</p>"""
    sort_by: NotRequired["aws_sdk_codecommit.types.sort_by_enum.SortByEnum"]
    """<p>The criteria used to sort the results of a list repositories operation.</p>"""
    order: NotRequired["aws_sdk_codecommit.types.order_enum.OrderEnum"]
    """<p>The order in which to sort the results of a list repositories operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRepositoriesInput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "sort_by" in value:
        import aws_sdk_codecommit.types.sort_by_enum

        out["sortBy"] = aws_sdk_codecommit.types.sort_by_enum.serialize_aws_json_1_1(
            value["sort_by"]
        )
    if "order" in value:
        import aws_sdk_codecommit.types.order_enum

        out["order"] = aws_sdk_codecommit.types.order_enum.serialize_aws_json_1_1(
            value["order"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRepositoriesInput:
    out: ListRepositoriesInput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "sortBy" in data:
        import aws_sdk_codecommit.types.sort_by_enum

        out["sort_by"] = aws_sdk_codecommit.types.sort_by_enum.deserialize_aws_json_1_1(
            data["sortBy"]
        )
    if "order" in data:
        import aws_sdk_codecommit.types.order_enum

        out["order"] = aws_sdk_codecommit.types.order_enum.deserialize_aws_json_1_1(
            data["order"]
        )
    return out
