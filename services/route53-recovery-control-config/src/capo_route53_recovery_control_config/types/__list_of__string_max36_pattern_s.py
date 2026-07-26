"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#__listOf__stringMax36PatternS``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53_recovery_control_config.types.__string_max36_pattern_s

__listOf__stringMax36PatternS: TypeAlias = list[
    "capo_route53_recovery_control_config.types.__string_max36_pattern_s.__stringMax36PatternS"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOf__stringMax36PatternS) -> list:
    return list(value)


def deserialize_json(data: list) -> __listOf__stringMax36PatternS:
    return list(data)
