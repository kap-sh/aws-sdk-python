"""Generated from Smithy shape ``com.amazonaws.connect#SearchableRoutingCriteria``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.searchable_routing_criteria_step_list


class SearchableRoutingCriteria(TypedDict):
    steps: NotRequired[
        "aws_sdk_connect.types.searchable_routing_criteria_step_list.SearchableRoutingCriteriaStepList"
    ]
    """<p>The list of Routing criteria steps of the contact routing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchableRoutingCriteria) -> dict:
    out: dict = {}
    if "steps" in value:
        import aws_sdk_connect.types.searchable_routing_criteria_step_list

        out["Steps"] = (
            aws_sdk_connect.types.searchable_routing_criteria_step_list.serialize_json(
                value["steps"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchableRoutingCriteria:
    out: SearchableRoutingCriteria = {}  # type: ignore[typeddict-item]
    if "Steps" in data:
        import aws_sdk_connect.types.searchable_routing_criteria_step_list

        out["steps"] = (
            aws_sdk_connect.types.searchable_routing_criteria_step_list.deserialize_json(
                data["Steps"]
            )
        )
    return out
