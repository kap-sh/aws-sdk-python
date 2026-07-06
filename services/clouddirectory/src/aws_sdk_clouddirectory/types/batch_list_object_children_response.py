"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchListObjectChildrenResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.link_name_to_object_identifier_map
    import aws_sdk_clouddirectory.types.next_token


class BatchListObjectChildrenResponse(TypedDict, closed=True):
    children: NotRequired[
        "aws_sdk_clouddirectory.types.link_name_to_object_identifier_map.LinkNameToObjectIdentifierMap"
    ]
    """<p>The children structure, which is a map with the key as the <code>LinkName</code> and <code>ObjectIdentifier</code> as the value.</p>"""
    next_token: NotRequired["aws_sdk_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchListObjectChildrenResponse) -> dict:
    out: dict = {}
    if "children" in value:
        import aws_sdk_clouddirectory.types.link_name_to_object_identifier_map

        out["Children"] = (
            aws_sdk_clouddirectory.types.link_name_to_object_identifier_map.serialize_json(
                value["children"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> BatchListObjectChildrenResponse:
    out: BatchListObjectChildrenResponse = {}  # type: ignore[typeddict-item]
    if "Children" in data:
        import aws_sdk_clouddirectory.types.link_name_to_object_identifier_map

        out["children"] = (
            aws_sdk_clouddirectory.types.link_name_to_object_identifier_map.deserialize_json(
                data["Children"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
