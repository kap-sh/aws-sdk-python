"""Generated from Smithy shape ``com.amazonaws.athena#NamedQueryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_athena.types.named_query

NamedQueryList: TypeAlias = list["aws_sdk_athena.types.named_query.NamedQuery"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NamedQueryList) -> list:
    import aws_sdk_athena.types.named_query

    out: list = []
    for item in value:
        out.append(aws_sdk_athena.types.named_query.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> NamedQueryList:
    import aws_sdk_athena.types.named_query

    out: NamedQueryList = []
    for item in data:
        out.append(aws_sdk_athena.types.named_query.deserialize_aws_json_1_1(item))
    return out
