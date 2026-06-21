"""Generated from Smithy shape ``com.amazonaws.eks#ClusterVersionStatus``."""

from typing import Literal, TypeAlias, cast

ClusterVersionStatus: TypeAlias = Literal[
    "unsupported",
    "standard-support",
    "extended-support",
]


# --- restJson1 ser/de ---
def serialize_json(value: ClusterVersionStatus) -> str:
    return value


def deserialize_json(data: str) -> ClusterVersionStatus:
    return cast(ClusterVersionStatus, data)
