"""Generated from Smithy shape ``com.amazonaws.rds#DescribeAccountAttributesMessage``."""

from typing import TypedDict

from aws_sdk_rds._protocol.xml import Element


class DescribeAccountAttributesMessage(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeAccountAttributesMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> DescribeAccountAttributesMessage:
    out: DescribeAccountAttributesMessage = {}  # type: ignore[typeddict-item]
    return out
