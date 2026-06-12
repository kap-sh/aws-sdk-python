"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#DomainList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_simspaceweaver.types.domain

DomainList: TypeAlias = list["aws_sdk_simspaceweaver.types.domain.Domain"]


# --- restJson1 ser/de ---
def serialize_json(value: DomainList) -> list:
    import aws_sdk_simspaceweaver.types.domain

    out: list = []
    for item in value:
        out.append(aws_sdk_simspaceweaver.types.domain.serialize_json(item))
    return out


def deserialize_json(data: list) -> DomainList:
    import aws_sdk_simspaceweaver.types.domain

    out: DomainList = []
    for item in data:
        out.append(aws_sdk_simspaceweaver.types.domain.deserialize_json(item))
    return out
