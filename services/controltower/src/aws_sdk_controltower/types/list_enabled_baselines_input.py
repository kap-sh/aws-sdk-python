"""Generated from Smithy shape ``com.amazonaws.controltower#ListEnabledBaselinesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_controltower.types.enabled_baseline_filter
    import aws_sdk_controltower.types.list_enabled_baselines_max_results
    import aws_sdk_controltower.types.list_enabled_baselines_next_token


class ListEnabledBaselinesInput(TypedDict):
    filter: NotRequired[
        "aws_sdk_controltower.types.enabled_baseline_filter.EnabledBaselineFilter"
    ]
    """<p>A filter applied on the <code>ListEnabledBaseline</code> operation. Allowed filters are <code>baselineIdentifiers</code> and <code>targetIdentifiers</code>. The filter can be applied for either, or both.</p>"""
    next_token: NotRequired[
        "aws_sdk_controltower.types.list_enabled_baselines_next_token.ListEnabledBaselinesNextToken"
    ]
    """<p>A pagination token.</p>"""
    max_results: NotRequired[
        "aws_sdk_controltower.types.list_enabled_baselines_max_results.ListEnabledBaselinesMaxResults"
    ]
    """<p>The maximum number of results to be shown.</p>"""
    include_children: "bool"
    """<p>A value that can be set to include the child enabled baselines in responses. The default value is false.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEnabledBaselinesInput) -> dict:
    out: dict = {}
    if "filter" in value:
        import aws_sdk_controltower.types.enabled_baseline_filter

        out["filter"] = (
            aws_sdk_controltower.types.enabled_baseline_filter.serialize_json(
                value["filter"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    out["includeChildren"] = value.get("include_children", False)
    return out


def deserialize_json(data: dict) -> ListEnabledBaselinesInput:
    out: ListEnabledBaselinesInput = {}  # type: ignore[typeddict-item]
    if "filter" in data:
        import aws_sdk_controltower.types.enabled_baseline_filter

        out["filter"] = (
            aws_sdk_controltower.types.enabled_baseline_filter.deserialize_json(
                data["filter"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "includeChildren" in data:
        out["include_children"] = data["includeChildren"]
    else:
        out["include_children"] = False
    return out
