"""Generated from Smithy shape ``com.amazonaws.rtbfabric#FilterConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.filter

FilterConfiguration: TypeAlias = list["aws_sdk_rtbfabric.types.filter.Filter"]


# --- restJson1 ser/de ---
def serialize_json(value: FilterConfiguration) -> list:
    import aws_sdk_rtbfabric.types.filter

    out: list = []
    for item in value:
        out.append(aws_sdk_rtbfabric.types.filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> FilterConfiguration:
    import aws_sdk_rtbfabric.types.filter

    out: FilterConfiguration = []
    for item in data:
        out.append(aws_sdk_rtbfabric.types.filter.deserialize_json(item))
    return out
