"""Generated from Smithy shape ``com.amazonaws.inspector2#NetworkPath``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.step_list


class NetworkPath(TypedDict, closed=True):
    steps: NotRequired["capo_inspector2.types.step_list.StepList"]
    """<p>The details on the steps in the network path.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkPath) -> dict:
    out: dict = {}
    if "steps" in value:
        import capo_inspector2.types.step_list

        out["steps"] = capo_inspector2.types.step_list.serialize_json(value["steps"])
    return out


def deserialize_json(data: dict) -> NetworkPath:
    out: NetworkPath = {}  # type: ignore[typeddict-item]
    if "steps" in data:
        import capo_inspector2.types.step_list

        out["steps"] = capo_inspector2.types.step_list.deserialize_json(data["steps"])
    return out
