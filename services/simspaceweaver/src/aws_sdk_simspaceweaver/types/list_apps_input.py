"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#ListAppsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_simspaceweaver.types.optional_string
    import aws_sdk_simspaceweaver.types.positive_integer
    import aws_sdk_simspaceweaver.types.sim_space_weaver_resource_name


class ListAppsInput(TypedDict):
    simulation: "aws_sdk_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
    """<p>The name of the simulation that you want to list apps for.</p>"""
    domain: NotRequired[
        "aws_sdk_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
    ]
    """<p>The name of the domain that you want to list apps for.</p>"""
    max_results: NotRequired[
        "aws_sdk_simspaceweaver.types.positive_integer.PositiveInteger"
    ]
    """<p>The maximum number of apps to list.</p>"""
    next_token: NotRequired[
        "aws_sdk_simspaceweaver.types.optional_string.OptionalString"
    ]
    """<p>If SimSpace Weaver returns <code>nextToken</code>, then there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page, call the operation again using the returned token. Keep all other arguments unchanged. If no results remain, then <code>nextToken</code> is set to <code>null</code>. Each pagination token expires after 24 hours. If you provide a token that isn't valid, then you receive an <i>HTTP 400 ValidationException</i> error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAppsInput:
    out: ListAppsInput = {}  # type: ignore[typeddict-item]
    return out
