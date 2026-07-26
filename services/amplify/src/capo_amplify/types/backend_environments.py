"""Generated from Smithy shape ``com.amazonaws.amplify#BackendEnvironments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amplify.types.backend_environment

BackendEnvironments: TypeAlias = list[
    "capo_amplify.types.backend_environment.BackendEnvironment"
]


# --- restJson1 ser/de ---
def serialize_json(value: BackendEnvironments) -> list:
    import capo_amplify.types.backend_environment

    out: list = []
    for item in value:
        out.append(capo_amplify.types.backend_environment.serialize_json(item))
    return out


def deserialize_json(data: list) -> BackendEnvironments:
    import capo_amplify.types.backend_environment

    out: BackendEnvironments = []
    for item in data:
        out.append(capo_amplify.types.backend_environment.deserialize_json(item))
    return out
