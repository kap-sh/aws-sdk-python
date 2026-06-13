"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceReferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.service_reference

ServiceReferenceList: TypeAlias = list[
    "aws_sdk_resiliencehubv2.types.service_reference.ServiceReference"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceReferenceList) -> list:
    import aws_sdk_resiliencehubv2.types.service_reference

    out: list = []
    for item in value:
        out.append(aws_sdk_resiliencehubv2.types.service_reference.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServiceReferenceList:
    import aws_sdk_resiliencehubv2.types.service_reference

    out: ServiceReferenceList = []
    for item in data:
        out.append(
            aws_sdk_resiliencehubv2.types.service_reference.deserialize_json(item)
        )
    return out
