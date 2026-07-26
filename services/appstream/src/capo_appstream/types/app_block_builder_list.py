"""Generated from Smithy shape ``com.amazonaws.appstream#AppBlockBuilderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.app_block_builder

AppBlockBuilderList: TypeAlias = list[
    "capo_appstream.types.app_block_builder.AppBlockBuilder"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppBlockBuilderList) -> list:
    import capo_appstream.types.app_block_builder

    out: list = []
    for item in value:
        out.append(capo_appstream.types.app_block_builder.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AppBlockBuilderList:
    import capo_appstream.types.app_block_builder

    out: AppBlockBuilderList = []
    for item in data:
        out.append(
            capo_appstream.types.app_block_builder.deserialize_aws_json_1_1(item)
        )
    return out
