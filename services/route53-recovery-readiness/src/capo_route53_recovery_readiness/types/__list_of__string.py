"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#__listOf__string``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53_recovery_readiness.types.__string

__listOf__string: TypeAlias = list[
    "capo_route53_recovery_readiness.types.__string.__string"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOf__string) -> list:
    return list(value)


def deserialize_json(data: list) -> __listOf__string:
    return list(data)
