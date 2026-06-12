"""Generated from Smithy shape ``com.amazonaws.securityhub#AssociationSetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.association_set_details

AssociationSetList: TypeAlias = list[
    "aws_sdk_securityhub.types.association_set_details.AssociationSetDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociationSetList) -> list:
    import aws_sdk_securityhub.types.association_set_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.association_set_details.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AssociationSetList:
    import aws_sdk_securityhub.types.association_set_details

    out: AssociationSetList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.association_set_details.deserialize_json(item)
        )
    return out
