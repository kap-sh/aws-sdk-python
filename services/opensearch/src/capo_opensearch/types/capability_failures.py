"""Generated from Smithy shape ``com.amazonaws.opensearch#CapabilityFailures``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.capability_failure

CapabilityFailures: TypeAlias = list[
    "capo_opensearch.types.capability_failure.CapabilityFailure"
]


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityFailures) -> list:
    import capo_opensearch.types.capability_failure

    out: list = []
    for item in value:
        out.append(capo_opensearch.types.capability_failure.serialize_json(item))
    return out


def deserialize_json(data: list) -> CapabilityFailures:
    import capo_opensearch.types.capability_failure

    out: CapabilityFailures = []
    for item in data:
        out.append(capo_opensearch.types.capability_failure.deserialize_json(item))
    return out
