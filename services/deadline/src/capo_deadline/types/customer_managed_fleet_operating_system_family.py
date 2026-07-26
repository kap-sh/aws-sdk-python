"""Generated from Smithy shape ``com.amazonaws.deadline#CustomerManagedFleetOperatingSystemFamily``."""

from typing import Literal, TypeAlias, cast

CustomerManagedFleetOperatingSystemFamily: TypeAlias = Literal[
    "WINDOWS",
    "LINUX",
    "MACOS",
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomerManagedFleetOperatingSystemFamily) -> str:
    return value


def deserialize_json(data: str) -> CustomerManagedFleetOperatingSystemFamily:
    return cast(CustomerManagedFleetOperatingSystemFamily, data)
