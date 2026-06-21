"""Generated from Smithy shape ``com.amazonaws.cloudformation#OperationResultFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element

OperationResultFilterName: TypeAlias = Literal["OPERATION_RESULT_STATUS",]


# --- awsQuery ser/de ---
def to_query_text(value: OperationResultFilterName) -> str:
    return value


def from_query_text(text: str) -> OperationResultFilterName:
    return cast(OperationResultFilterName, text)


def serialize_query(
    value: OperationResultFilterName, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> OperationResultFilterName:
    return from_query_text(el.text or "")
