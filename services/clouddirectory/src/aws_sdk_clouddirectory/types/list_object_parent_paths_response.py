"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ListObjectParentPathsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.next_token
    import aws_sdk_clouddirectory.types.path_to_object_identifiers_list


class ListObjectParentPathsResponse(TypedDict, closed=True):
    path_to_object_identifiers_list: NotRequired[
        "aws_sdk_clouddirectory.types.path_to_object_identifiers_list.PathToObjectIdentifiersList"
    ]
    """<p>Returns the path to the <code>ObjectIdentifiers</code> that are associated with the directory.</p>"""
    next_token: NotRequired["aws_sdk_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListObjectParentPathsResponse) -> dict:
    out: dict = {}
    if "path_to_object_identifiers_list" in value:
        import aws_sdk_clouddirectory.types.path_to_object_identifiers_list

        out["PathToObjectIdentifiersList"] = (
            aws_sdk_clouddirectory.types.path_to_object_identifiers_list.serialize_json(
                value["path_to_object_identifiers_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListObjectParentPathsResponse:
    out: ListObjectParentPathsResponse = {}  # type: ignore[typeddict-item]
    if "PathToObjectIdentifiersList" in data:
        import aws_sdk_clouddirectory.types.path_to_object_identifiers_list

        out["path_to_object_identifiers_list"] = (
            aws_sdk_clouddirectory.types.path_to_object_identifiers_list.deserialize_json(
                data["PathToObjectIdentifiersList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
