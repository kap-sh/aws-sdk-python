"""Generated from Smithy shape ``com.amazonaws.bedrock#SortByProvisionedModels``."""

from typing import Literal, TypeAlias, cast

SortByProvisionedModels: TypeAlias = Literal["CreationTime",]


# --- restJson1 ser/de ---
def serialize_json(value: SortByProvisionedModels) -> str:
    return value


def deserialize_json(data: str) -> SortByProvisionedModels:
    return cast(SortByProvisionedModels, data)
