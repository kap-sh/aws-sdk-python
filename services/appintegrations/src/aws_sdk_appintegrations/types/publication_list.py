"""Generated from Smithy shape ``com.amazonaws.appintegrations#PublicationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.publication

PublicationList: TypeAlias = list[
    "aws_sdk_appintegrations.types.publication.Publication"
]


# --- restJson1 ser/de ---
def serialize_json(value: PublicationList) -> list:
    import aws_sdk_appintegrations.types.publication

    out: list = []
    for item in value:
        out.append(aws_sdk_appintegrations.types.publication.serialize_json(item))
    return out


def deserialize_json(data: list) -> PublicationList:
    import aws_sdk_appintegrations.types.publication

    out: PublicationList = []
    for item in data:
        out.append(aws_sdk_appintegrations.types.publication.deserialize_json(item))
    return out
