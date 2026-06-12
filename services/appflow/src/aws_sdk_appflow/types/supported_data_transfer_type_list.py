"""Generated from Smithy shape ``com.amazonaws.appflow#SupportedDataTransferTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appflow.types.supported_data_transfer_type

SupportedDataTransferTypeList: TypeAlias = list[
    "aws_sdk_appflow.types.supported_data_transfer_type.SupportedDataTransferType"
]


# --- restJson1 ser/de ---
def serialize_json(value: SupportedDataTransferTypeList) -> list:
    import aws_sdk_appflow.types.supported_data_transfer_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_appflow.types.supported_data_transfer_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SupportedDataTransferTypeList:
    import aws_sdk_appflow.types.supported_data_transfer_type

    out: SupportedDataTransferTypeList = []
    for item in data:
        out.append(
            aws_sdk_appflow.types.supported_data_transfer_type.deserialize_json(item)
        )
    return out
