"""Generated from Smithy shape ``com.amazonaws.mpa#AdditionalSecurityRequirements``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mpa.types.additional_security_requirement

AdditionalSecurityRequirements: TypeAlias = list[
    "capo_mpa.types.additional_security_requirement.AdditionalSecurityRequirement"
]


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalSecurityRequirements) -> list:
    import capo_mpa.types.additional_security_requirement

    out: list = []
    for item in value:
        out.append(capo_mpa.types.additional_security_requirement.serialize_json(item))
    return out


def deserialize_json(data: list) -> AdditionalSecurityRequirements:
    import capo_mpa.types.additional_security_requirement

    out: AdditionalSecurityRequirements = []
    for item in data:
        out.append(
            capo_mpa.types.additional_security_requirement.deserialize_json(item)
        )
    return out
