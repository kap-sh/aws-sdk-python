"""Generated from Smithy shape ``com.amazonaws.kendra#SharePointUrlList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.url

SharePointUrlList: TypeAlias = list["capo_kendra.types.url.Url"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SharePointUrlList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SharePointUrlList:
    return list(data)
