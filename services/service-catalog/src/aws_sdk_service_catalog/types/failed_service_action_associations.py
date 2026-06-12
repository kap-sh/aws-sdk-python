"""Generated from Smithy shape ``com.amazonaws.servicecatalog#FailedServiceActionAssociations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.failed_service_action_association

FailedServiceActionAssociations: TypeAlias = list[
    "aws_sdk_service_catalog.types.failed_service_action_association.FailedServiceActionAssociation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailedServiceActionAssociations) -> list:
    import aws_sdk_service_catalog.types.failed_service_action_association

    out: list = []
    for item in value:
        out.append(
            aws_sdk_service_catalog.types.failed_service_action_association.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FailedServiceActionAssociations:
    import aws_sdk_service_catalog.types.failed_service_action_association

    out: FailedServiceActionAssociations = []
    for item in data:
        out.append(
            aws_sdk_service_catalog.types.failed_service_action_association.deserialize_aws_json_1_1(
                item
            )
        )
    return out
