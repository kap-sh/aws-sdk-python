"""Generated from Smithy shape ``com.amazonaws.securityhub#UnprocessedStandardsControlAssociations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.unprocessed_standards_control_association

UnprocessedStandardsControlAssociations: TypeAlias = list[
    "aws_sdk_securityhub.types.unprocessed_standards_control_association.UnprocessedStandardsControlAssociation"
]


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessedStandardsControlAssociations) -> list:
    import aws_sdk_securityhub.types.unprocessed_standards_control_association

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.unprocessed_standards_control_association.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> UnprocessedStandardsControlAssociations:
    import aws_sdk_securityhub.types.unprocessed_standards_control_association

    out: UnprocessedStandardsControlAssociations = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.unprocessed_standards_control_association.deserialize_json(
                item
            )
        )
    return out
