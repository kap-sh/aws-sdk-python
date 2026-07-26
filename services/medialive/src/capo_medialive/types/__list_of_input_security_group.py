"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfInputSecurityGroup``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.input_security_group

__listOfInputSecurityGroup: TypeAlias = list[
    "capo_medialive.types.input_security_group.InputSecurityGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfInputSecurityGroup) -> list:
    import capo_medialive.types.input_security_group

    out: list = []
    for item in value:
        out.append(capo_medialive.types.input_security_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfInputSecurityGroup:
    import capo_medialive.types.input_security_group

    out: __listOfInputSecurityGroup = []
    for item in data:
        out.append(capo_medialive.types.input_security_group.deserialize_json(item))
    return out
