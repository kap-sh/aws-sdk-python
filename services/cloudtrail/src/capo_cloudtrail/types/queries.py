"""Generated from Smithy shape ``com.amazonaws.cloudtrail#Queries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudtrail.types.query

Queries: TypeAlias = list["capo_cloudtrail.types.query.Query"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Queries) -> list:
    import capo_cloudtrail.types.query

    out: list = []
    for item in value:
        out.append(capo_cloudtrail.types.query.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Queries:
    import capo_cloudtrail.types.query

    out: Queries = []
    for item in data:
        out.append(capo_cloudtrail.types.query.deserialize_aws_json_1_1(item))
    return out
