"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfAutomatedAbrRule``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.automated_abr_rule

__listOfAutomatedAbrRule: TypeAlias = list[
    "aws_sdk_mediaconvert.types.automated_abr_rule.AutomatedAbrRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfAutomatedAbrRule) -> list:
    import aws_sdk_mediaconvert.types.automated_abr_rule

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconvert.types.automated_abr_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfAutomatedAbrRule:
    import aws_sdk_mediaconvert.types.automated_abr_rule

    out: __listOfAutomatedAbrRule = []
    for item in data:
        out.append(aws_sdk_mediaconvert.types.automated_abr_rule.deserialize_json(item))
    return out
