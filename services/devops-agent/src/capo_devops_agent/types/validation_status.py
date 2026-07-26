"""Generated from Smithy shape ``com.amazonaws.devopsagent#ValidationStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>Represents the validation state of an association.</p>"""
ValidationStatus: TypeAlias = Literal[
    "valid",
    "invalid",
    "pending-confirmation",
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationStatus) -> str:
    return value


def deserialize_json(data: str) -> ValidationStatus:
    return cast(ValidationStatus, data)
