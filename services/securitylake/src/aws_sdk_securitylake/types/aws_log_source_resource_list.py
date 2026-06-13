"""Generated from Smithy shape ``com.amazonaws.securitylake#AwsLogSourceResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.aws_log_source_resource

AwsLogSourceResourceList: TypeAlias = list[
    "aws_sdk_securitylake.types.aws_log_source_resource.AwsLogSourceResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsLogSourceResourceList) -> list:
    import aws_sdk_securitylake.types.aws_log_source_resource

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securitylake.types.aws_log_source_resource.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AwsLogSourceResourceList:
    import aws_sdk_securitylake.types.aws_log_source_resource

    out: AwsLogSourceResourceList = []
    for item in data:
        out.append(
            aws_sdk_securitylake.types.aws_log_source_resource.deserialize_json(item)
        )
    return out
