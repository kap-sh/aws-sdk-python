"""Generated from Smithy shape ``com.amazonaws.mpa#IdentitySources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mpa.types.identity_source_for_list

IdentitySources: TypeAlias = list[
    "aws_sdk_mpa.types.identity_source_for_list.IdentitySourceForList"
]


# --- restJson1 ser/de ---
def serialize_json(value: IdentitySources) -> list:
    import aws_sdk_mpa.types.identity_source_for_list

    out: list = []
    for item in value:
        out.append(aws_sdk_mpa.types.identity_source_for_list.serialize_json(item))
    return out


def deserialize_json(data: list) -> IdentitySources:
    import aws_sdk_mpa.types.identity_source_for_list

    out: IdentitySources = []
    for item in data:
        out.append(aws_sdk_mpa.types.identity_source_for_list.deserialize_json(item))
    return out
