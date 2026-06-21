"""Generated from Smithy shape ``com.amazonaws.iot#AwsJobAbortCriteriaAbortAction``."""

from typing import Literal, TypeAlias, cast

AwsJobAbortCriteriaAbortAction: TypeAlias = Literal["CANCEL",]


# --- restJson1 ser/de ---
def serialize_json(value: AwsJobAbortCriteriaAbortAction) -> str:
    return value


def deserialize_json(data: str) -> AwsJobAbortCriteriaAbortAction:
    return cast(AwsJobAbortCriteriaAbortAction, data)
