"""Generated from Smithy shape ``com.amazonaws.kendra#SuggestableConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.suggestable_config

SuggestableConfigList: TypeAlias = list[
    "aws_sdk_kendra.types.suggestable_config.SuggestableConfig"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SuggestableConfigList) -> list:
    import aws_sdk_kendra.types.suggestable_config

    out: list = []
    for item in value:
        out.append(aws_sdk_kendra.types.suggestable_config.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SuggestableConfigList:
    import aws_sdk_kendra.types.suggestable_config

    out: SuggestableConfigList = []
    for item in data:
        out.append(
            aws_sdk_kendra.types.suggestable_config.deserialize_aws_json_1_1(item)
        )
    return out
