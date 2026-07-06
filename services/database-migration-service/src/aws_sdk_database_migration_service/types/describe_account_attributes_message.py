"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeAccountAttributesMessage``."""

from typing_extensions import TypedDict


class DescribeAccountAttributesMessage(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAccountAttributesMessage) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAccountAttributesMessage:
    out: DescribeAccountAttributesMessage = {}  # type: ignore[typeddict-item]
    return out
