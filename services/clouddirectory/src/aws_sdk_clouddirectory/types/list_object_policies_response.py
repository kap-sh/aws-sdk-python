"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ListObjectPoliciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.next_token
    import aws_sdk_clouddirectory.types.object_identifier_list


class ListObjectPoliciesResponse(TypedDict, closed=True):
    attached_policy_ids: NotRequired[
        "aws_sdk_clouddirectory.types.object_identifier_list.ObjectIdentifierList"
    ]
    """<p>A list of policy <code>ObjectIdentifiers</code>, that are attached to the object.</p>"""
    next_token: NotRequired["aws_sdk_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListObjectPoliciesResponse) -> dict:
    out: dict = {}
    if "attached_policy_ids" in value:
        import aws_sdk_clouddirectory.types.object_identifier_list

        out["AttachedPolicyIds"] = (
            aws_sdk_clouddirectory.types.object_identifier_list.serialize_json(
                value["attached_policy_ids"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListObjectPoliciesResponse:
    out: ListObjectPoliciesResponse = {}  # type: ignore[typeddict-item]
    if "AttachedPolicyIds" in data:
        import aws_sdk_clouddirectory.types.object_identifier_list

        out["attached_policy_ids"] = (
            aws_sdk_clouddirectory.types.object_identifier_list.deserialize_json(
                data["AttachedPolicyIds"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
