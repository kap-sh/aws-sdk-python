"""Generated from Smithy shape ``com.amazonaws.connecthealth#CustomTemplateBase``."""

from typing import Literal, TypeAlias, cast

CustomTemplateBase: TypeAlias = Literal[
    "HISTORY_AND_PHYSICAL",
    "GIRPP",
    "DAP",
    "SIRP",
    "BIRP",
    "BEHAVIORAL_SOAP",
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomTemplateBase) -> str:
    return value


def deserialize_json(data: str) -> CustomTemplateBase:
    return cast(CustomTemplateBase, data)
