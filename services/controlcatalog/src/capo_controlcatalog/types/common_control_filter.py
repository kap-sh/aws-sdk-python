"""Generated from Smithy shape ``com.amazonaws.controlcatalog#CommonControlFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controlcatalog.types.objective_resource_filter_list


class CommonControlFilter(TypedDict, closed=True):
    objectives: NotRequired[
        "capo_controlcatalog.types.objective_resource_filter_list.ObjectiveResourceFilterList"
    ]
    """<p>The objective that's used as filter criteria.</p> <p>You can use this parameter to specify one objective ARN at a time. Passing multiple ARNs in the <code>CommonControlFilter</code> isn’t supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CommonControlFilter) -> dict:
    out: dict = {}
    if "objectives" in value:
        import capo_controlcatalog.types.objective_resource_filter_list

        out["Objectives"] = (
            capo_controlcatalog.types.objective_resource_filter_list.serialize_json(
                value["objectives"]
            )
        )
    return out


def deserialize_json(data: dict) -> CommonControlFilter:
    out: CommonControlFilter = {}  # type: ignore[typeddict-item]
    if "Objectives" in data:
        import capo_controlcatalog.types.objective_resource_filter_list

        out["objectives"] = (
            capo_controlcatalog.types.objective_resource_filter_list.deserialize_json(
                data["Objectives"]
            )
        )
    return out
