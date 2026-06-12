"""Generated from Smithy shape ``com.amazonaws.xray#RetrievedServicesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_xray.types.retrieved_service

RetrievedServicesList: TypeAlias = list[
    "aws_sdk_xray.types.retrieved_service.RetrievedService"
]


# --- restJson1 ser/de ---
def serialize_json(value: RetrievedServicesList) -> list:
    import aws_sdk_xray.types.retrieved_service

    out: list = []
    for item in value:
        out.append(aws_sdk_xray.types.retrieved_service.serialize_json(item))
    return out


def deserialize_json(data: list) -> RetrievedServicesList:
    import aws_sdk_xray.types.retrieved_service

    out: RetrievedServicesList = []
    for item in data:
        out.append(aws_sdk_xray.types.retrieved_service.deserialize_json(item))
    return out
