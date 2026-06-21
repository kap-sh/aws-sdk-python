"""Generated from Smithy shape ``com.amazonaws.deadline#ServiceManagedFleetOperatingSystemFamily``."""

from typing import Literal, TypeAlias, cast

ServiceManagedFleetOperatingSystemFamily: TypeAlias = Literal[
    "WINDOWS",
    "LINUX",
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceManagedFleetOperatingSystemFamily) -> str:
    return value


def deserialize_json(data: str) -> ServiceManagedFleetOperatingSystemFamily:
    return cast(ServiceManagedFleetOperatingSystemFamily, data)
