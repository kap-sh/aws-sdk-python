"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PortalSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.portal_summary

PortalSummaries: TypeAlias = list[
    "aws_sdk_iotsitewise.types.portal_summary.PortalSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PortalSummaries) -> list:
    import aws_sdk_iotsitewise.types.portal_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_iotsitewise.types.portal_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> PortalSummaries:
    import aws_sdk_iotsitewise.types.portal_summary

    out: PortalSummaries = []
    for item in data:
        out.append(aws_sdk_iotsitewise.types.portal_summary.deserialize_json(item))
    return out
