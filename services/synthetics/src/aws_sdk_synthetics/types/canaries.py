"""Generated from Smithy shape ``com.amazonaws.synthetics#Canaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.canary

Canaries: TypeAlias = list["aws_sdk_synthetics.types.canary.Canary"]


# --- restJson1 ser/de ---
def serialize_json(value: Canaries) -> list:
    import aws_sdk_synthetics.types.canary

    out: list = []
    for item in value:
        out.append(aws_sdk_synthetics.types.canary.serialize_json(item))
    return out


def deserialize_json(data: list) -> Canaries:
    import aws_sdk_synthetics.types.canary

    out: Canaries = []
    for item in data:
        out.append(aws_sdk_synthetics.types.canary.deserialize_json(item))
    return out
