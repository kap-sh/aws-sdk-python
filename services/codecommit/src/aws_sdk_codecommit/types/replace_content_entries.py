"""Generated from Smithy shape ``com.amazonaws.codecommit#ReplaceContentEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.replace_content_entry

ReplaceContentEntries: TypeAlias = list[
    "aws_sdk_codecommit.types.replace_content_entry.ReplaceContentEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplaceContentEntries) -> list:
    import aws_sdk_codecommit.types.replace_content_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codecommit.types.replace_content_entry.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReplaceContentEntries:
    import aws_sdk_codecommit.types.replace_content_entry

    out: ReplaceContentEntries = []
    for item in data:
        out.append(
            aws_sdk_codecommit.types.replace_content_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
