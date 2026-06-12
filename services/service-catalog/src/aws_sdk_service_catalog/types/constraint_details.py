"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ConstraintDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.constraint_detail

ConstraintDetails: TypeAlias = list[
    "aws_sdk_service_catalog.types.constraint_detail.ConstraintDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConstraintDetails) -> list:
    import aws_sdk_service_catalog.types.constraint_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_service_catalog.types.constraint_detail.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConstraintDetails:
    import aws_sdk_service_catalog.types.constraint_detail

    out: ConstraintDetails = []
    for item in data:
        out.append(
            aws_sdk_service_catalog.types.constraint_detail.deserialize_aws_json_1_1(
                item
            )
        )
    return out
