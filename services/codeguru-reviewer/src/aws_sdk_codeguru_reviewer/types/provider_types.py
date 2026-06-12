"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#ProviderTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeguru_reviewer.types.provider_type

ProviderTypes: TypeAlias = list[
    "aws_sdk_codeguru_reviewer.types.provider_type.ProviderType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProviderTypes) -> list:
    import aws_sdk_codeguru_reviewer.types.provider_type

    out: list = []
    for item in value:
        out.append(aws_sdk_codeguru_reviewer.types.provider_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProviderTypes:
    import aws_sdk_codeguru_reviewer.types.provider_type

    out: ProviderTypes = []
    for item in data:
        out.append(aws_sdk_codeguru_reviewer.types.provider_type.deserialize_json(item))
    return out
