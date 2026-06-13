"""Generated from Smithy shape ``com.amazonaws.qconnect#RetrieveResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.retrieve_result

RetrieveResultList: TypeAlias = list[
    "aws_sdk_qconnect.types.retrieve_result.RetrieveResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: RetrieveResultList) -> list:
    import aws_sdk_qconnect.types.retrieve_result

    out: list = []
    for item in value:
        out.append(aws_sdk_qconnect.types.retrieve_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> RetrieveResultList:
    import aws_sdk_qconnect.types.retrieve_result

    out: RetrieveResultList = []
    for item in data:
        out.append(aws_sdk_qconnect.types.retrieve_result.deserialize_json(item))
    return out
