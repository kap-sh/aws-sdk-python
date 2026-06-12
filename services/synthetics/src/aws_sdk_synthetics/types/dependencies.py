"""Generated from Smithy shape ``com.amazonaws.synthetics#Dependencies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.dependency

Dependencies: TypeAlias = list["aws_sdk_synthetics.types.dependency.Dependency"]


# --- restJson1 ser/de ---
def serialize_json(value: Dependencies) -> list:
    import aws_sdk_synthetics.types.dependency

    out: list = []
    for item in value:
        out.append(aws_sdk_synthetics.types.dependency.serialize_json(item))
    return out


def deserialize_json(data: list) -> Dependencies:
    import aws_sdk_synthetics.types.dependency

    out: Dependencies = []
    for item in data:
        out.append(aws_sdk_synthetics.types.dependency.deserialize_json(item))
    return out
