"""Generated from Smithy shape ``com.amazonaws.qbusiness#Retrievers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.retriever

Retrievers: TypeAlias = list["aws_sdk_qbusiness.types.retriever.Retriever"]


# --- restJson1 ser/de ---
def serialize_json(value: Retrievers) -> list:
    import aws_sdk_qbusiness.types.retriever

    out: list = []
    for item in value:
        out.append(aws_sdk_qbusiness.types.retriever.serialize_json(item))
    return out


def deserialize_json(data: list) -> Retrievers:
    import aws_sdk_qbusiness.types.retriever

    out: Retrievers = []
    for item in data:
        out.append(aws_sdk_qbusiness.types.retriever.deserialize_json(item))
    return out
