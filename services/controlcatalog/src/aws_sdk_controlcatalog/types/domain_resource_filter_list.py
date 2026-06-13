"""Generated from Smithy shape ``com.amazonaws.controlcatalog#DomainResourceFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_controlcatalog.types.domain_resource_filter

DomainResourceFilterList: TypeAlias = list[
    "aws_sdk_controlcatalog.types.domain_resource_filter.DomainResourceFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainResourceFilterList) -> list:
    import aws_sdk_controlcatalog.types.domain_resource_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_controlcatalog.types.domain_resource_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DomainResourceFilterList:
    import aws_sdk_controlcatalog.types.domain_resource_filter

    out: DomainResourceFilterList = []
    for item in data:
        out.append(
            aws_sdk_controlcatalog.types.domain_resource_filter.deserialize_json(item)
        )
    return out
