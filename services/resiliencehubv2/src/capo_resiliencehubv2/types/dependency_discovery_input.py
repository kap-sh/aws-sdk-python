"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DependencyDiscoveryInput``."""

from typing import Literal, TypeAlias, cast

"""<p>Caller-settable values for dependency discovery. INITIALIZING is system-managed.</p>"""
DependencyDiscoveryInput: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DependencyDiscoveryInput) -> str:
    return value


def deserialize_json(data: str) -> DependencyDiscoveryInput:
    return cast(DependencyDiscoveryInput, data)
