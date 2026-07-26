"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#ListListenersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.generic_string
    import capo_global_accelerator.types.listeners


class ListListenersResponse(TypedDict, closed=True):
    listeners: NotRequired["capo_global_accelerator.types.listeners.Listeners"]
    """<p>The list of listeners for an accelerator.</p>"""
    next_token: NotRequired[
        "capo_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListListenersResponse) -> dict:
    out: dict = {}
    if "listeners" in value:
        import capo_global_accelerator.types.listeners

        out["Listeners"] = (
            capo_global_accelerator.types.listeners.serialize_aws_json_1_1(
                value["listeners"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListListenersResponse:
    out: ListListenersResponse = {}  # type: ignore[typeddict-item]
    if "Listeners" in data:
        import capo_global_accelerator.types.listeners

        out["listeners"] = (
            capo_global_accelerator.types.listeners.deserialize_aws_json_1_1(
                data["Listeners"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
