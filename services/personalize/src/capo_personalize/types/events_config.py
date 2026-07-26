"""Generated from Smithy shape ``com.amazonaws.personalize#EventsConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.event_parameters_list


class EventsConfig(TypedDict, closed=True):
    event_parameters_list: NotRequired[
        "capo_personalize.types.event_parameters_list.EventParametersList"
    ]
    """<p>A list of event parameters, which includes event types and their event value thresholds and weights.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventsConfig) -> dict:
    out: dict = {}
    if "event_parameters_list" in value:
        import capo_personalize.types.event_parameters_list

        out["eventParametersList"] = (
            capo_personalize.types.event_parameters_list.serialize_aws_json_1_1(
                value["event_parameters_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EventsConfig:
    out: EventsConfig = {}  # type: ignore[typeddict-item]
    if "eventParametersList" in data:
        import capo_personalize.types.event_parameters_list

        out["event_parameters_list"] = (
            capo_personalize.types.event_parameters_list.deserialize_aws_json_1_1(
                data["eventParametersList"]
            )
        )
    return out
