"""Generated from Smithy shape ``com.amazonaws.configservice#SourceDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.source_detail

SourceDetails: TypeAlias = list[
    "aws_sdk_config_service.types.source_detail.SourceDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceDetails) -> list:
    import aws_sdk_config_service.types.source_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_config_service.types.source_detail.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SourceDetails:
    import aws_sdk_config_service.types.source_detail

    out: SourceDetails = []
    for item in data:
        out.append(
            aws_sdk_config_service.types.source_detail.deserialize_aws_json_1_1(item)
        )
    return out
