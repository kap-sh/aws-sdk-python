"""Generated from Smithy shape ``com.amazonaws.qbusiness#DataAccessorExternalIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.data_accessor_external_id

DataAccessorExternalIds: TypeAlias = list[
    "aws_sdk_qbusiness.types.data_accessor_external_id.DataAccessorExternalId"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataAccessorExternalIds) -> list:
    return list(value)


def deserialize_json(data: list) -> DataAccessorExternalIds:
    return list(data)
