"""Generated from Smithy shape ``com.amazonaws.emrserverless#ApplicationStateSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr_serverless.types.application_state

ApplicationStateSet: TypeAlias = list[
    "capo_emr_serverless.types.application_state.ApplicationState"
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationStateSet) -> list:
    return list(value)


def deserialize_json(data: list) -> ApplicationStateSet:
    return list(data)
