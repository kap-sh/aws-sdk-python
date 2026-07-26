"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#RxNormEntityCategory``."""

from typing import Literal, TypeAlias, cast

RxNormEntityCategory: TypeAlias = Literal["MEDICATION",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RxNormEntityCategory) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RxNormEntityCategory:
    return cast(RxNormEntityCategory, data)
