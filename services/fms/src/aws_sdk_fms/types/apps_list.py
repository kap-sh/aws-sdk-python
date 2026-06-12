"""Generated from Smithy shape ``com.amazonaws.fms#AppsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fms.types.app

AppsList: TypeAlias = list["aws_sdk_fms.types.app.App"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppsList) -> list:
    import aws_sdk_fms.types.app

    out: list = []
    for item in value:
        out.append(aws_sdk_fms.types.app.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AppsList:
    import aws_sdk_fms.types.app

    out: AppsList = []
    for item in data:
        out.append(aws_sdk_fms.types.app.deserialize_aws_json_1_1(item))
    return out
