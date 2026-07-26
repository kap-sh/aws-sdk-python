"""Generated from Smithy shape ``com.amazonaws.directconnect#LoaContentType``."""

from typing import Literal, TypeAlias, cast

LoaContentType: TypeAlias = Literal["application/pdf",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoaContentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LoaContentType:
    return cast(LoaContentType, data)
