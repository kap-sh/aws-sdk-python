"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfSuppressDataIdentifier``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_macie2.types.suppress_data_identifier

__listOfSuppressDataIdentifier: TypeAlias = list[
    "aws_sdk_macie2.types.suppress_data_identifier.SuppressDataIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfSuppressDataIdentifier) -> list:
    import aws_sdk_macie2.types.suppress_data_identifier

    out: list = []
    for item in value:
        out.append(aws_sdk_macie2.types.suppress_data_identifier.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfSuppressDataIdentifier:
    import aws_sdk_macie2.types.suppress_data_identifier

    out: __listOfSuppressDataIdentifier = []
    for item in data:
        out.append(aws_sdk_macie2.types.suppress_data_identifier.deserialize_json(item))
    return out
