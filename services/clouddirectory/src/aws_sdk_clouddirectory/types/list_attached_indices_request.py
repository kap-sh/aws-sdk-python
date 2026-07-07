"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ListAttachedIndicesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn
    import aws_sdk_clouddirectory.types.consistency_level
    import aws_sdk_clouddirectory.types.next_token
    import aws_sdk_clouddirectory.types.number_results
    import aws_sdk_clouddirectory.types.object_reference


class ListAttachedIndicesRequest(TypedDict, closed=True):
    directory_arn: "aws_sdk_clouddirectory.types.arn.Arn"
    """<p>The ARN of the directory.</p>"""
    target_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference"
    """<p>A reference to the object that has indices attached.</p>"""
    next_token: NotRequired["aws_sdk_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""
    max_results: NotRequired[
        "aws_sdk_clouddirectory.types.number_results.NumberResults"
    ]
    """<p>The maximum number of results to retrieve.</p>"""
    consistency_level: NotRequired[
        "aws_sdk_clouddirectory.types.consistency_level.ConsistencyLevel"
    ]
    """<p>The consistency level to use for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAttachedIndicesRequest) -> dict:
    out: dict = {}
    import aws_sdk_clouddirectory.types.object_reference

    out["TargetReference"] = (
        aws_sdk_clouddirectory.types.object_reference.serialize_json(
            value["target_reference"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListAttachedIndicesRequest:
    out: ListAttachedIndicesRequest = {}  # type: ignore[typeddict-item]
    if "TargetReference" in data:
        import aws_sdk_clouddirectory.types.object_reference

        out["target_reference"] = (
            aws_sdk_clouddirectory.types.object_reference.deserialize_json(
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
