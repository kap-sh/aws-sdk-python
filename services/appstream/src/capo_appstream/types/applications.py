"""Generated from Smithy shape ``com.amazonaws.appstream#Applications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.application

Applications: TypeAlias = list["capo_appstream.types.application.Application"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Applications) -> list:
    import capo_appstream.types.application

    out: list = []
    for item in value:
        out.append(capo_appstream.types.application.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Applications:
    import capo_appstream.types.application

    out: Applications = []
    for item in data:
        out.append(capo_appstream.types.application.deserialize_aws_json_1_1(item))
    return out
