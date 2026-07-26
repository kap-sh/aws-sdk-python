"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ListAttachedIndicesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn
    import capo_clouddirectory.types.consistency_level
    import capo_clouddirectory.types.next_token
    import capo_clouddirectory.types.number_results
    import capo_clouddirectory.types.object_reference


class ListAttachedIndicesRequest(TypedDict, closed=True):
    directory_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The ARN of the directory.</p>"""
    target_reference: "capo_clouddirectory.types.object_reference.ObjectReference"
    """<p>A reference to the object that has indices attached.</p>"""
    next_token: NotRequired["capo_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""
    max_results: NotRequired["capo_clouddirectory.types.number_results.NumberResults"]
    """<p>The maximum number of results to retrieve.</p>"""
    consistency_level: NotRequired[
        "capo_clouddirectory.types.consistency_level.ConsistencyLevel"
    ]
    """<p>The consistency level to use for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAttachedIndicesRequest) -> dict:
    out: dict = {}
    import capo_clouddirectory.types.object_reference

    out["TargetReference"] = capo_clouddirectory.types.object_reference.serialize_json(
        value["target_reference"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListAttachedIndicesRequest:
    out: ListAttachedIndicesRequest = {}  # type: ignore[typeddict-item]
    if "TargetReference" in data:
        import capo_clouddirectory.types.object_reference

        out["target_reference"] = (
            capo_clouddirectory.types.object_reference.deserialize_json(
                data["TargetReference"]
            )
        )
    else:
        raise DeserializationError(
            "ListAttachedIndicesRequest.target_reference required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
