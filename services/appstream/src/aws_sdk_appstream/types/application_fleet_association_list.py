"""Generated from Smithy shape ``com.amazonaws.appstream#ApplicationFleetAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appstream.types.application_fleet_association

ApplicationFleetAssociationList: TypeAlias = list[
    "aws_sdk_appstream.types.application_fleet_association.ApplicationFleetAssociation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationFleetAssociationList) -> list:
    import aws_sdk_appstream.types.application_fleet_association

    out: list = []
    for item in value:
        out.append(
            aws_sdk_appstream.types.application_fleet_association.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ApplicationFleetAssociationList:
    import aws_sdk_appstream.types.application_fleet_association

    out: ApplicationFleetAssociationList = []
    for item in data:
        out.append(
            aws_sdk_appstream.types.application_fleet_association.deserialize_aws_json_1_1(
                item
            )
        )
    return out
