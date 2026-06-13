"""Generated from Smithy shape ``com.amazonaws.inspector2#CountsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.counts

CountsList: TypeAlias = list["aws_sdk_inspector2.types.counts.Counts"]


# --- restJson1 ser/de ---
def serialize_json(value: CountsList) -> list:
    import aws_sdk_inspector2.types.counts

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector2.types.counts.serialize_json(item))
    return out


def deserialize_json(data: list) -> CountsList:
    import aws_sdk_inspector2.types.counts

    out: CountsList = []
    for item in data:
        out.append(aws_sdk_inspector2.types.counts.deserialize_json(item))
    return out
