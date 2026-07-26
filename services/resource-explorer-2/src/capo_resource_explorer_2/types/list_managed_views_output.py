"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ListManagedViewsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_explorer_2.types.managed_view_arn_list


class ListManagedViewsOutput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>. The pagination tokens expire after 24 hours.</p>"""
    managed_views: NotRequired[
        "capo_resource_explorer_2.types.managed_view_arn_list.ManagedViewArnList"
    ]
    """<p>The list of managed views available in the Amazon Web Services Region in which you called this operation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagedViewsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "managed_views" in value:
        import capo_resource_explorer_2.types.managed_view_arn_list

        out["ManagedViews"] = (
            capo_resource_explorer_2.types.managed_view_arn_list.serialize_json(
                value["managed_views"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListManagedViewsOutput:
    out: ListManagedViewsOutput = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ManagedViews" in data:
        import capo_resource_explorer_2.types.managed_view_arn_list

        out["managed_views"] = (
            capo_resource_explorer_2.types.managed_view_arn_list.deserialize_json(
                data["ManagedViews"]
            )
        )
    return out
