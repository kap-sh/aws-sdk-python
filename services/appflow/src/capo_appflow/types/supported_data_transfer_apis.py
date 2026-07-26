"""Generated from Smithy shape ``com.amazonaws.appflow#SupportedDataTransferApis``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appflow.types.data_transfer_api

SupportedDataTransferApis: TypeAlias = list[
    "capo_appflow.types.data_transfer_api.DataTransferApi"
]


# --- restJson1 ser/de ---
def serialize_json(value: SupportedDataTransferApis) -> list:
    import capo_appflow.types.data_transfer_api

    out: list = []
    for item in value:
        out.append(capo_appflow.types.data_transfer_api.serialize_json(item))
    return out


def deserialize_json(data: list) -> SupportedDataTransferApis:
    import capo_appflow.types.data_transfer_api

    out: SupportedDataTransferApis = []
    for item in data:
        out.append(capo_appflow.types.data_transfer_api.deserialize_json(item))
    return out
