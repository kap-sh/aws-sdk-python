"""Generated from Smithy shape ``com.amazonaws.appflow#SupportedDataTransferApis``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appflow.types.data_transfer_api

SupportedDataTransferApis: TypeAlias = list[
    "aws_sdk_appflow.types.data_transfer_api.DataTransferApi"
]


# --- restJson1 ser/de ---
def serialize_json(value: SupportedDataTransferApis) -> list:
    import aws_sdk_appflow.types.data_transfer_api

    out: list = []
    for item in value:
        out.append(aws_sdk_appflow.types.data_transfer_api.serialize_json(item))
    return out


def deserialize_json(data: list) -> SupportedDataTransferApis:
    import aws_sdk_appflow.types.data_transfer_api

    out: SupportedDataTransferApis = []
    for item in data:
        out.append(aws_sdk_appflow.types.data_transfer_api.deserialize_json(item))
    return out
