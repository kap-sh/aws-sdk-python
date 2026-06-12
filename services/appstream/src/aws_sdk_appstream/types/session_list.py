"""Generated from Smithy shape ``com.amazonaws.appstream#SessionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appstream.types.session

SessionList: TypeAlias = list["aws_sdk_appstream.types.session.Session"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionList) -> list:
    import aws_sdk_appstream.types.session

    out: list = []
    for item in value:
        out.append(aws_sdk_appstream.types.session.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SessionList:
    import aws_sdk_appstream.types.session

    out: SessionList = []
    for item in data:
        out.append(aws_sdk_appstream.types.session.deserialize_aws_json_1_1(item))
    return out
