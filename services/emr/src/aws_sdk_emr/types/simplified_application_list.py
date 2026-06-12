"""Generated from Smithy shape ``com.amazonaws.emr#SimplifiedApplicationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr.types.simplified_application

SimplifiedApplicationList: TypeAlias = list[
    "aws_sdk_emr.types.simplified_application.SimplifiedApplication"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SimplifiedApplicationList) -> list:
    import aws_sdk_emr.types.simplified_application

    out: list = []
    for item in value:
        out.append(
            aws_sdk_emr.types.simplified_application.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SimplifiedApplicationList:
    import aws_sdk_emr.types.simplified_application

    out: SimplifiedApplicationList = []
    for item in data:
        out.append(
            aws_sdk_emr.types.simplified_application.deserialize_aws_json_1_1(item)
        )
    return out
