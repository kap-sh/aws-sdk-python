"""Generated from Smithy shape ``com.amazonaws.securityhub#StandardsControlAssociationDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.standards_control_association_detail

StandardsControlAssociationDetails: TypeAlias = list[
    "aws_sdk_securityhub.types.standards_control_association_detail.StandardsControlAssociationDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: StandardsControlAssociationDetails) -> list:
    import aws_sdk_securityhub.types.standards_control_association_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.standards_control_association_detail.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> StandardsControlAssociationDetails:
    import aws_sdk_securityhub.types.standards_control_association_detail

    out: StandardsControlAssociationDetails = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.standards_control_association_detail.deserialize_json(
                item
            )
        )
    return out
