"""Generated from Smithy shape ``com.amazonaws.athena#NamedQueryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_athena.types.named_query

NamedQueryList: TypeAlias = list["capo_athena.types.named_query.NamedQuery"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NamedQueryList) -> list:
    import capo_athena.types.named_query

    out: list = []
    for item in value:
        out.append(capo_athena.types.named_query.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> NamedQueryList:
    import capo_athena.types.named_query

    out: NamedQueryList = []
    for item in data:
        out.append(capo_athena.types.named_query.deserialize_aws_json_1_1(item))
    return out
