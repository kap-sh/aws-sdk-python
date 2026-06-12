"""Generated from Smithy shape ``com.amazonaws.securityhub#StandardsControlAssociationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.standards_control_association_summary

StandardsControlAssociationSummaries: TypeAlias = list[
    "aws_sdk_securityhub.types.standards_control_association_summary.StandardsControlAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: StandardsControlAssociationSummaries) -> list:
    import aws_sdk_securityhub.types.standards_control_association_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.standards_control_association_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> StandardsControlAssociationSummaries:
    import aws_sdk_securityhub.types.standards_control_association_summary

    out: StandardsControlAssociationSummaries = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.standards_control_association_summary.deserialize_json(
                item
            )
        )
    return out
