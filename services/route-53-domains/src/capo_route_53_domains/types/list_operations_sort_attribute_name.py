"""Generated from Smithy shape ``com.amazonaws.route53domains#ListOperationsSortAttributeName``."""

from typing import Literal, TypeAlias, cast

ListOperationsSortAttributeName: TypeAlias = Literal["SubmittedDate",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOperationsSortAttributeName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ListOperationsSortAttributeName:
    return cast(ListOperationsSortAttributeName, data)
