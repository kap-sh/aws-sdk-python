"""Generated from Smithy shape ``com.amazonaws.emrcontainers#EndpointStates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr_containers.types.endpoint_state

EndpointStates: TypeAlias = list[
    "capo_emr_containers.types.endpoint_state.EndpointState"
]


# --- restJson1 ser/de ---
def serialize_json(value: EndpointStates) -> list:
    import capo_emr_containers.types.endpoint_state

    out: list = []
    for item in value:
        out.append(capo_emr_containers.types.endpoint_state.serialize_json(item))
    return out


def deserialize_json(data: list) -> EndpointStates:
    import capo_emr_containers.types.endpoint_state

    out: EndpointStates = []
    for item in data:
        out.append(capo_emr_containers.types.endpoint_state.deserialize_json(item))
    return out
