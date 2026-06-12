"""Generated from Smithy shape ``com.amazonaws.controltower#ListEnabledControlsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_controltower.types.enabled_control_filter
    import aws_sdk_controltower.types.max_results
    import aws_sdk_controltower.types.target_identifier


class ListEnabledControlsInput(TypedDict):
    target_identifier: NotRequired[
        "aws_sdk_controltower.types.target_identifier.TargetIdentifier"
    ]
    """<p>The ARN of the organizational unit. For information on how to find the <code>targetIdentifier</code>, see <a href=\"https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html\">the overview page</a>.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to continue the list from a previous API call with the same parameters.</p>"""
    max_results: NotRequired["aws_sdk_controltower.types.max_results.MaxResults"]
    """<p>How many results to return per API call.</p>"""
    filter: NotRequired[
        "aws_sdk_controltower.types.enabled_control_filter.EnabledControlFilter"
    ]
    """<p>An input filter for the <code>ListEnabledControls</code> API that lets you select the types of control operations to view.</p>"""
    include_children: "bool"
    """<p>A boolean value that determines whether to include enabled controls from child organizational units in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEnabledControlsInput) -> dict:
    out: dict = {}
    if "target_identifier" in value:
        out["targetIdentifier"] = value["target_identifier"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "filter" in value:
        import aws_sdk_controltower.types.enabled_control_filter

        out["filter"] = (
            aws_sdk_controltower.types.enabled_control_filter.serialize_json(
                value["filter"]
            )
        )
    out["includeChildren"] = value.get("include_children", False)
    return out


def deserialize_json(data: dict) -> ListEnabledControlsInput:
    out: ListEnabledControlsInput = {}  # type: ignore[typeddict-item]
    if "targetIdentifier" in data:
        out["target_identifier"] = data["targetIdentifier"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "filter" in data:
        import aws_sdk_controltower.types.enabled_control_filter

        out["filter"] = (
            aws_sdk_controltower.types.enabled_control_filter.deserialize_json(
                data["filter"]
            )
        )
    if "includeChildren" in data:
        out["include_children"] = data["includeChildren"]
    else:
        out["include_children"] = False
    return out
