"""Generated from Smithy shape ``com.amazonaws.ecs#ListTaskDefinitionFamiliesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_list


class ListTaskDefinitionFamiliesResponse(TypedDict, closed=True):
    families: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>The list of task definition family names that match the <code>ListTaskDefinitionFamilies</code> request.</p>"""
    next_token: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListTaskDefinitionFamilies</code> request. When the results of a <code>ListTaskDefinitionFamilies</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTaskDefinitionFamiliesResponse) -> dict:
    out: dict = {}
    if "families" in value:
        import aws_sdk_ecs.types.string_list

        out["families"] = aws_sdk_ecs.types.string_list.serialize_aws_json_1_1(
            value["families"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTaskDefinitionFamiliesResponse:
    out: ListTaskDefinitionFamiliesResponse = {}  # type: ignore[typeddict-item]
    if "families" in data:
        import aws_sdk_ecs.types.string_list

        out["families"] = aws_sdk_ecs.types.string_list.deserialize_aws_json_1_1(
            data["families"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
