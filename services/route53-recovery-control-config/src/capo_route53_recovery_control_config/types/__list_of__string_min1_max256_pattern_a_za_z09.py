"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#__listOf__stringMin1Max256PatternAZaZ09``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09

__listOf__stringMin1Max256PatternAZaZ09: TypeAlias = list[
    "capo_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09.__stringMin1Max256PatternAZaZ09"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOf__stringMin1Max256PatternAZaZ09) -> list:
    return list(value)


def deserialize_json(data: list) -> __listOf__stringMin1Max256PatternAZaZ09:
    return list(data)
