"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ListServiceViewsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resource_explorer_2.types.service_view_arn_list


class ListServiceViewsOutput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The pagination token to use in a subsequent <code>ListServiceViews</code> request to retrieve the next set of results.</p>"""
    service_views: NotRequired[
        "aws_sdk_resource_explorer_2.types.service_view_arn_list.ServiceViewArnList"
    ]
    """<p>A list of Amazon Resource Names (ARNs) for the service views available in the current Amazon Web Services account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceViewsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "service_views" in value:
        import aws_sdk_resource_explorer_2.types.service_view_arn_list

        out["ServiceViews"] = (
            aws_sdk_resource_explorer_2.types.service_view_arn_list.serialize_json(
                value["service_views"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListServiceViewsOutput:
    out: ListServiceViewsOutput = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ServiceViews" in data:
        import aws_sdk_resource_explorer_2.types.service_view_arn_list

        out["service_views"] = (
            aws_sdk_resource_explorer_2.types.service_view_arn_list.deserialize_json(
                data["ServiceViews"]
            )
        )
    return out
