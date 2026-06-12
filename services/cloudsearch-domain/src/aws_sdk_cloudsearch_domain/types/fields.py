"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#Fields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudsearch_domain.types.string
    import aws_sdk_cloudsearch_domain.types.field_value

Fields: TypeAlias = dict[
    "aws_sdk_cloudsearch_domain.types.string.String",
    "aws_sdk_cloudsearch_domain.types.field_value.FieldValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Fields) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_cloudsearch_domain.types.field_value

        out[key] = aws_sdk_cloudsearch_domain.types.field_value.serialize_json(value)
    return out


def deserialize_json(data: dict) -> Fields:
    out: Fields = {}
    for key, value in data.items():
        import aws_sdk_cloudsearch_domain.types.field_value

        out[key] = aws_sdk_cloudsearch_domain.types.field_value.deserialize_json(value)
    return out
