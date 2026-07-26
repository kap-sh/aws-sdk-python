"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchListPolicyAttachmentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.next_token
    import capo_clouddirectory.types.object_identifier_list


class BatchListPolicyAttachmentsResponse(TypedDict, closed=True):
    object_identifiers: NotRequired[
        "capo_clouddirectory.types.object_identifier_list.ObjectIdentifierList"
    ]
    """<p>A list of <code>ObjectIdentifiers</code> to which the policy is attached.</p>"""
    next_token: NotRequired["capo_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchListPolicyAttachmentsResponse) -> dict:
    out: dict = {}
    if "object_identifiers" in value:
        import capo_clouddirectory.types.object_identifier_list

        out["ObjectIdentifiers"] = (
            capo_clouddirectory.types.object_identifier_list.serialize_json(
                value["object_identifiers"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> BatchListPolicyAttachmentsResponse:
    out: BatchListPolicyAttachmentsResponse = {}  # type: ignore[typeddict-item]
    if "ObjectIdentifiers" in data:
        import capo_clouddirectory.types.object_identifier_list

        out["object_identifiers"] = (
            capo_clouddirectory.types.object_identifier_list.deserialize_json(
                data["ObjectIdentifiers"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
