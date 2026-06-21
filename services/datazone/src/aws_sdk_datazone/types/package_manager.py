"""Generated from Smithy shape ``com.amazonaws.datazone#PackageManager``."""

from typing import Literal, TypeAlias, cast

"""<p>The package manager for a notebook run environment in Amazon SageMaker Unified Studio.</p>"""
PackageManager: TypeAlias = Literal["UV",]


# --- restJson1 ser/de ---
def serialize_json(value: PackageManager) -> str:
    return value


def deserialize_json(data: str) -> PackageManager:
    return cast(PackageManager, data)
