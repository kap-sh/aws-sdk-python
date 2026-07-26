"""Generated from Smithy shape ``com.amazonaws.panorama#ReportedRuntimeContextStates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_panorama.types.reported_runtime_context_state

ReportedRuntimeContextStates: TypeAlias = list[
    "capo_panorama.types.reported_runtime_context_state.ReportedRuntimeContextState"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReportedRuntimeContextStates) -> list:
    import capo_panorama.types.reported_runtime_context_state

    out: list = []
    for item in value:
        out.append(
            capo_panorama.types.reported_runtime_context_state.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ReportedRuntimeContextStates:
    import capo_panorama.types.reported_runtime_context_state

    out: ReportedRuntimeContextStates = []
    for item in data:
        out.append(
            capo_panorama.types.reported_runtime_context_state.deserialize_json(item)
        )
    return out
