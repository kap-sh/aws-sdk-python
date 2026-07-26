"""Generated from Smithy shape ``com.amazonaws.workdocs#AdditionalResponseFieldType``."""

from typing import Literal, TypeAlias, cast

AdditionalResponseFieldType: TypeAlias = Literal["WEBURL",]


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalResponseFieldType) -> str:
    return value


def deserialize_json(data: str) -> AdditionalResponseFieldType:
    return cast(AdditionalResponseFieldType, data)
