"""Generated from Smithy shape ``com.amazonaws.appstream#Applications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appstream.types.application

Applications: TypeAlias = list["aws_sdk_appstream.types.application.Application"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Applications) -> list:
    import aws_sdk_appstream.types.application

    out: list = []
    for item in value:
        out.append(aws_sdk_appstream.types.application.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Applications:
    import aws_sdk_appstream.types.application

    out: Applications = []
    for item in data:
        out.append(aws_sdk_appstream.types.application.deserialize_aws_json_1_1(item))
    return out
