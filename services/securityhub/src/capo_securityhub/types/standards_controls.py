"""Generated from Smithy shape ``com.amazonaws.securityhub#StandardsControls``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.standards_control

StandardsControls: TypeAlias = list[
    "capo_securityhub.types.standards_control.StandardsControl"
]


# --- restJson1 ser/de ---
def serialize_json(value: StandardsControls) -> list:
    import capo_securityhub.types.standards_control

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.standards_control.serialize_json(item))
    return out


def deserialize_json(data: list) -> StandardsControls:
    import capo_securityhub.types.standards_control

    out: StandardsControls = []
    for item in data:
        out.append(capo_securityhub.types.standards_control.deserialize_json(item))
    return out
