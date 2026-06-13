"""Generated from Smithy shape ``com.amazonaws.qconnect#RetrievalFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.retrieval_filter_configuration

RetrievalFilterList: TypeAlias = list[
    "aws_sdk_qconnect.types.retrieval_filter_configuration.RetrievalFilterConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalFilterList) -> list:
    import aws_sdk_qconnect.types.retrieval_filter_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_qconnect.types.retrieval_filter_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RetrievalFilterList:
    import aws_sdk_qconnect.types.retrieval_filter_configuration

    out: RetrievalFilterList = []
    for item in data:
        out.append(
            aws_sdk_qconnect.types.retrieval_filter_configuration.deserialize_json(item)
        )
    return out
