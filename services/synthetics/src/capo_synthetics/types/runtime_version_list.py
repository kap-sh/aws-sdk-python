"""Generated from Smithy shape ``com.amazonaws.synthetics#RuntimeVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_synthetics.types.runtime_version

RuntimeVersionList: TypeAlias = list[
    "capo_synthetics.types.runtime_version.RuntimeVersion"
]


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeVersionList) -> list:
    import capo_synthetics.types.runtime_version

    out: list = []
    for item in value:
        out.append(capo_synthetics.types.runtime_version.serialize_json(item))
    return out


def deserialize_json(data: list) -> RuntimeVersionList:
    import capo_synthetics.types.runtime_version

    out: RuntimeVersionList = []
    for item in data:
        out.append(capo_synthetics.types.runtime_version.deserialize_json(item))
    return out
