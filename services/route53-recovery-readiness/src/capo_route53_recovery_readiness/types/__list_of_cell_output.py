"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#__listOfCellOutput``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53_recovery_readiness.types.cell_output

__listOfCellOutput: TypeAlias = list[
    "capo_route53_recovery_readiness.types.cell_output.CellOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfCellOutput) -> list:
    import capo_route53_recovery_readiness.types.cell_output

    out: list = []
    for item in value:
        out.append(
            capo_route53_recovery_readiness.types.cell_output.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfCellOutput:
    import capo_route53_recovery_readiness.types.cell_output

    out: __listOfCellOutput = []
    for item in data:
        out.append(
            capo_route53_recovery_readiness.types.cell_output.deserialize_json(item)
        )
    return out
