"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CmafWriteDASHManifest``."""

from typing import Literal, TypeAlias, cast

"""When set to ENABLED, a DASH MPD manifest will be generated for this output."""
CmafWriteDASHManifest: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CmafWriteDASHManifest) -> str:
    return value


def deserialize_json(data: str) -> CmafWriteDASHManifest:
    return cast(CmafWriteDASHManifest, data)
