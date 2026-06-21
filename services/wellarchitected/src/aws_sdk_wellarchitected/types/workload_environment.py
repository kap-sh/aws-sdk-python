"""Generated from Smithy shape ``com.amazonaws.wellarchitected#WorkloadEnvironment``."""

from typing import Literal, TypeAlias, cast

"""<p>The environment for the workload.</p>"""
WorkloadEnvironment: TypeAlias = Literal[
    "PRODUCTION",
    "PREPRODUCTION",
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadEnvironment) -> str:
    return value


def deserialize_json(data: str) -> WorkloadEnvironment:
    return cast(WorkloadEnvironment, data)
