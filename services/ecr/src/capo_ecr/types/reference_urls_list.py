"""Generated from Smithy shape ``com.amazonaws.ecr#ReferenceUrlsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr.types.url

ReferenceUrlsList: TypeAlias = list["capo_ecr.types.url.Url"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReferenceUrlsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ReferenceUrlsList:
    return list(data)
