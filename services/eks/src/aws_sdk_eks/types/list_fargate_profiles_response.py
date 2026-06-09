"""Generated from Smithy shape ``com.amazonaws.eks#ListFargateProfilesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.string
    import aws_sdk_eks.types.string_list


class ListFargateProfilesResponse(TypedDict):
    fargate_profile_names: NotRequired["aws_sdk_eks.types.string_list.StringList"]
    """<p>A list of all of the Fargate profiles associated with the specified cluster.</p>"""
    next_token: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a previous paginated request, where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is null when there are no more results to return.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFargateProfilesResponse) -> dict:
    out: dict = {}
    if "fargate_profile_names" in value:
        import aws_sdk_eks.types.string_list

        out["fargateProfileNames"] = aws_sdk_eks.types.string_list.serialize_json(
            value["fargate_profile_names"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFargateProfilesResponse:
    out: ListFargateProfilesResponse = {}  # type: ignore[typeddict-item]
    if "fargateProfileNames" in data:
        import aws_sdk_eks.types.string_list

        out["fargate_profile_names"] = aws_sdk_eks.types.string_list.deserialize_json(
            data["fargateProfileNames"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
