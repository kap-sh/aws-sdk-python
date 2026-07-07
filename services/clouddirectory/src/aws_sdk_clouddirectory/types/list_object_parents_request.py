"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ListObjectParentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn
    import aws_sdk_clouddirectory.types.bool
    import aws_sdk_clouddirectory.types.consistency_level
    import aws_sdk_clouddirectory.types.next_token
    import aws_sdk_clouddirectory.types.number_results
    import aws_sdk_clouddirectory.types.object_reference


class ListObjectParentsRequest(TypedDict, closed=True):
    directory_arn: "aws_sdk_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where the object resides. For more information, see <a>arns</a>.</p>"""
    object_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference"
    """<p>The reference that identifies the object for which parent objects are being listed.</p>"""
    next_token: NotRequired["aws_sdk_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""
    max_results: NotRequired[
        "aws_sdk_clouddirectory.types.number_results.NumberResults"
    ]
    """<p>The maximum number of items to be retrieved in a single call. This is an approximate number.</p>"""
    consistency_level: NotRequired[
        "aws_sdk_clouddirectory.types.consistency_level.ConsistencyLevel"
    ]
    """<p>Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.</p>"""
    include_all_links_to_each_parent: "aws_sdk_clouddirectory.types.bool.Bool"
    """<p>When set to True, returns all <a>ListObjectParentsResponse$ParentLinks</a>. There could be multiple links between a parent-child pair.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListObjectParentsRequest) -> dict:
    out: dict = {}
    import aws_sdk_clouddirectory.types.object_reference

    out["ObjectReference"] = (
        aws_sdk_clouddirectory.types.object_reference.serialize_json(
            value["object_reference"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    out["IncludeAllLinksToEachParent"] = value.get(
        "include_all_links_to_each_parent", False
    )
    return out


def deserialize_json(data: dict) -> ListObjectParentsRequest:
    out: ListObjectParentsRequest = {}  # type: ignore[typeddict-item]
    if "ObjectReference" in data:
        import aws_sdk_clouddirectory.types.object_reference

        out["object_reference"] = (
            aws_sdk_clouddirectory.types.object_reference.deserialize_json(
                data["ObjectReference"]
            )
        )
    else:
        raise DeserializationError("ListObjectParentsRequest.object_reference required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "IncludeAllLinksToEachParent" in data:
        out["include_all_links_to_each_parent"] = data["IncludeAllLinksToEachParent"]
    else:
        out["include_all_links_to_each_parent"] = False
    return out
