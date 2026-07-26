"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ListPolicyAttachmentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn
    import capo_clouddirectory.types.consistency_level
    import capo_clouddirectory.types.next_token
    import capo_clouddirectory.types.number_results
    import capo_clouddirectory.types.object_reference


class ListPolicyAttachmentsRequest(TypedDict, closed=True):
    directory_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where objects reside. For more information, see <a>arns</a>.</p>"""
    policy_reference: "capo_clouddirectory.types.object_reference.ObjectReference"
    """<p>The reference that identifies the policy object.</p>"""
    next_token: NotRequired["capo_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""
    max_results: NotRequired["capo_clouddirectory.types.number_results.NumberResults"]
    """<p>The maximum number of items to be retrieved in a single call. This is an approximate number.</p>"""
    consistency_level: NotRequired[
        "capo_clouddirectory.types.consistency_level.ConsistencyLevel"
    ]
    """<p>Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPolicyAttachmentsRequest) -> dict:
    out: dict = {}
    import capo_clouddirectory.types.object_reference

    out["PolicyReference"] = capo_clouddirectory.types.object_reference.serialize_json(
        value["policy_reference"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListPolicyAttachmentsRequest:
    out: ListPolicyAttachmentsRequest = {}  # type: ignore[typeddict-item]
    if "PolicyReference" in data:
        import capo_clouddirectory.types.object_reference

        out["policy_reference"] = (
            capo_clouddirectory.types.object_reference.deserialize_json(
                data["PolicyReference"]
            )
        )
    else:
        raise DeserializationError(
            "ListPolicyAttachmentsRequest.policy_reference required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
