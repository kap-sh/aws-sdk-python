"""Generated from Smithy shape ``com.amazonaws.emr#ListBootstrapActionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.command_list
    import capo_emr.types.marker


class ListBootstrapActionsOutput(TypedDict, closed=True):
    bootstrap_actions: NotRequired["capo_emr.types.command_list.CommandList"]
    """<p>The bootstrap actions associated with the cluster.</p>"""
    marker: NotRequired["capo_emr.types.marker.Marker"]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListBootstrapActionsOutput) -> dict:
    out: dict = {}
    if "bootstrap_actions" in value:
        import capo_emr.types.command_list

        out["BootstrapActions"] = capo_emr.types.command_list.serialize_aws_json_1_1(
            value["bootstrap_actions"]
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListBootstrapActionsOutput:
    out: ListBootstrapActionsOutput = {}  # type: ignore[typeddict-item]
    if "BootstrapActions" in data:
        import capo_emr.types.command_list

        out["bootstrap_actions"] = capo_emr.types.command_list.deserialize_aws_json_1_1(
            data["BootstrapActions"]
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
