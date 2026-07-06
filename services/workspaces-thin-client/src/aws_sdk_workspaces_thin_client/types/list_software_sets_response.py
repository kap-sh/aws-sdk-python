"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#ListSoftwareSetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_thin_client.types.pagination_token
    import aws_sdk_workspaces_thin_client.types.software_set_list


class ListSoftwareSetsResponse(TypedDict, closed=True):
    software_sets: NotRequired[
        "aws_sdk_workspaces_thin_client.types.software_set_list.SoftwareSetList"
    ]
    """<p>Describes software sets.</p>"""
    next_token: NotRequired[
        "aws_sdk_workspaces_thin_client.types.pagination_token.PaginationToken"
    ]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken error</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSoftwareSetsResponse) -> dict:
    out: dict = {}
    if "software_sets" in value:
        import aws_sdk_workspaces_thin_client.types.software_set_list

        out["softwareSets"] = (
            aws_sdk_workspaces_thin_client.types.software_set_list.serialize_json(
                value["software_sets"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSoftwareSetsResponse:
    out: ListSoftwareSetsResponse = {}  # type: ignore[typeddict-item]
    if "softwareSets" in data:
        import aws_sdk_workspaces_thin_client.types.software_set_list

        out["software_sets"] = (
            aws_sdk_workspaces_thin_client.types.software_set_list.deserialize_json(
                data["softwareSets"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
