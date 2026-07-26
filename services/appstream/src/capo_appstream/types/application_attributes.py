"""Generated from Smithy shape ``com.amazonaws.appstream#ApplicationAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.application_attribute

ApplicationAttributes: TypeAlias = list[
    "capo_appstream.types.application_attribute.ApplicationAttribute"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationAttributes) -> list:
    import capo_appstream.types.application_attribute

    out: list = []
    for item in value:
        out.append(
            capo_appstream.types.application_attribute.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ApplicationAttributes:
    import capo_appstream.types.application_attribute

    out: ApplicationAttributes = []
    for item in data:
        out.append(
            capo_appstream.types.application_attribute.deserialize_aws_json_1_1(item)
        )
    return out
