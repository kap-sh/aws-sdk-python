"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfMatchingResource``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_macie2.types.matching_resource

__listOfMatchingResource: TypeAlias = list[
    "aws_sdk_macie2.types.matching_resource.MatchingResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfMatchingResource) -> list:
    import aws_sdk_macie2.types.matching_resource

    out: list = []
    for item in value:
        out.append(aws_sdk_macie2.types.matching_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfMatchingResource:
    import aws_sdk_macie2.types.matching_resource

    out: __listOfMatchingResource = []
    for item in data:
        out.append(aws_sdk_macie2.types.matching_resource.deserialize_json(item))
    return out
