"""Generated from Smithy shape ``com.amazonaws.workmail#ListResourceDelegatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.next_token
    import capo_workmail.types.resource_delegates


class ListResourceDelegatesResponse(TypedDict, closed=True):
    delegates: NotRequired["capo_workmail.types.resource_delegates.ResourceDelegates"]
    """<p>One page of the resource's delegates.</p>"""
    next_token: NotRequired["capo_workmail.types.next_token.NextToken"]
    """<p>The token used to paginate through the delegates associated with a resource. While results are still available, it has an associated value. When the last page is reached, the token is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourceDelegatesResponse) -> dict:
    out: dict = {}
    if "delegates" in value:
        import capo_workmail.types.resource_delegates

        out["Delegates"] = (
            capo_workmail.types.resource_delegates.serialize_aws_json_1_1(
                value["delegates"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResourceDelegatesResponse:
    out: ListResourceDelegatesResponse = {}  # type: ignore[typeddict-item]
    if "Delegates" in data:
        import capo_workmail.types.resource_delegates

        out["delegates"] = (
            capo_workmail.types.resource_delegates.deserialize_aws_json_1_1(
                data["Delegates"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
