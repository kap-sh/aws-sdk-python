"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#FindingIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeguru_security.types.finding_identifier

FindingIdentifiers: TypeAlias = list[
    "aws_sdk_codeguru_security.types.finding_identifier.FindingIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingIdentifiers) -> list:
    import aws_sdk_codeguru_security.types.finding_identifier

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codeguru_security.types.finding_identifier.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FindingIdentifiers:
    import aws_sdk_codeguru_security.types.finding_identifier

    out: FindingIdentifiers = []
    for item in data:
        out.append(
            aws_sdk_codeguru_security.types.finding_identifier.deserialize_json(item)
        )
    return out
