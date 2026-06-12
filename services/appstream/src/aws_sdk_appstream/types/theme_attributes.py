"""Generated from Smithy shape ``com.amazonaws.appstream#ThemeAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appstream.types.theme_attribute

ThemeAttributes: TypeAlias = list[
    "aws_sdk_appstream.types.theme_attribute.ThemeAttribute"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThemeAttributes) -> list:
    import aws_sdk_appstream.types.theme_attribute

    out: list = []
    for item in value:
        out.append(aws_sdk_appstream.types.theme_attribute.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ThemeAttributes:
    import aws_sdk_appstream.types.theme_attribute

    out: ThemeAttributes = []
    for item in data:
        out.append(
            aws_sdk_appstream.types.theme_attribute.deserialize_aws_json_1_1(item)
        )
    return out
