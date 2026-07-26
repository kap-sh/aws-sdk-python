"""Generated from Smithy shape ``com.amazonaws.clouddirectory#LookupPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn
    import capo_clouddirectory.types.next_token
    import capo_clouddirectory.types.number_results
    import capo_clouddirectory.types.object_reference


class LookupPolicyRequest(TypedDict, closed=True):
    directory_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that is associated with the <a>Directory</a>. For more information, see <a>arns</a>.</p>"""
    object_reference: "capo_clouddirectory.types.object_reference.ObjectReference"
    """<p>Reference that identifies the object whose policies will be looked up.</p>"""
    next_token: NotRequired["capo_clouddirectory.types.next_token.NextToken"]
    """<p>The token to request the next page of results.</p>"""
    max_results: NotRequired["capo_clouddirectory.types.number_results.NumberResults"]
    """<p>The maximum number of items to be retrieved in a single call. This is an approximate number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LookupPolicyRequest) -> dict:
    out: dict = {}
    import capo_clouddirectory.types.object_reference

    out["ObjectReference"] = capo_clouddirectory.types.object_reference.serialize_json(
        value["object_reference"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> LookupPolicyRequest:
    out: LookupPolicyRequest = {}  # type: ignore[typeddict-item]
    if "ObjectReference" in data:
        import capo_clouddirectory.types.object_reference

        out["object_reference"] = (
            capo_clouddirectory.types.object_reference.deserialize_json(
                data["ObjectReference"]
            )
        )
    else:
        raise DeserializationError("LookupPolicyRequest.object_reference required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
