"""Generated from Smithy shape ``com.amazonaws.kendra#SeedUrlList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.seed_url

SeedUrlList: TypeAlias = list["capo_kendra.types.seed_url.SeedUrl"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SeedUrlList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SeedUrlList:
    return list(data)
