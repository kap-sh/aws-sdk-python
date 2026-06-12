"""Generated from Smithy shape ``com.amazonaws.kendra#FaqIdsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.faq_id

FaqIdsList: TypeAlias = list["aws_sdk_kendra.types.faq_id.FaqId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FaqIdsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> FaqIdsList:
    return list(data)
