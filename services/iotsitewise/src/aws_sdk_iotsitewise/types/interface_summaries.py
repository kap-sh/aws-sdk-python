"""Generated from Smithy shape ``com.amazonaws.iotsitewise#InterfaceSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.interface_summary

InterfaceSummaries: TypeAlias = list[
    "aws_sdk_iotsitewise.types.interface_summary.InterfaceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: InterfaceSummaries) -> list:
    import aws_sdk_iotsitewise.types.interface_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_iotsitewise.types.interface_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> InterfaceSummaries:
    import aws_sdk_iotsitewise.types.interface_summary

    out: InterfaceSummaries = []
    for item in data:
        out.append(aws_sdk_iotsitewise.types.interface_summary.deserialize_json(item))
    return out
