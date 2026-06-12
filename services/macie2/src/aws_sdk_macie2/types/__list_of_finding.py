"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfFinding``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_macie2.types.finding

__listOfFinding: TypeAlias = list["aws_sdk_macie2.types.finding.Finding"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfFinding) -> list:
    import aws_sdk_macie2.types.finding

    out: list = []
    for item in value:
        out.append(aws_sdk_macie2.types.finding.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfFinding:
    import aws_sdk_macie2.types.finding

    out: __listOfFinding = []
    for item in data:
        out.append(aws_sdk_macie2.types.finding.deserialize_json(item))
    return out
