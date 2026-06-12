"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SessionSpecifications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.session_specification

SessionSpecifications: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.session_specification.SessionSpecification"
]


# --- restJson1 ser/de ---
def serialize_json(value: SessionSpecifications) -> list:
    import aws_sdk_lex_models_v2.types.session_specification

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.session_specification.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SessionSpecifications:
    import aws_sdk_lex_models_v2.types.session_specification

    out: SessionSpecifications = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.session_specification.deserialize_json(item)
        )
    return out
