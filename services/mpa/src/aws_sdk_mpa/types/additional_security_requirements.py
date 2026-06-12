"""Generated from Smithy shape ``com.amazonaws.mpa#AdditionalSecurityRequirements``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mpa.types.additional_security_requirement

AdditionalSecurityRequirements: TypeAlias = list[
    "aws_sdk_mpa.types.additional_security_requirement.AdditionalSecurityRequirement"
]


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalSecurityRequirements) -> list:
    import aws_sdk_mpa.types.additional_security_requirement

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mpa.types.additional_security_requirement.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AdditionalSecurityRequirements:
    import aws_sdk_mpa.types.additional_security_requirement

    out: AdditionalSecurityRequirements = []
    for item in data:
        out.append(
            aws_sdk_mpa.types.additional_security_requirement.deserialize_json(item)
        )
    return out
