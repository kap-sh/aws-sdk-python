"""Generated from Smithy shape ``com.amazonaws.appflow#SalesforceDataTransferApiList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appflow.types.salesforce_data_transfer_api

SalesforceDataTransferApiList: TypeAlias = list[
    "aws_sdk_appflow.types.salesforce_data_transfer_api.SalesforceDataTransferApi"
]


# --- restJson1 ser/de ---
def serialize_json(value: SalesforceDataTransferApiList) -> list:
    import aws_sdk_appflow.types.salesforce_data_transfer_api

    out: list = []
    for item in value:
        out.append(
            aws_sdk_appflow.types.salesforce_data_transfer_api.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SalesforceDataTransferApiList:
    import aws_sdk_appflow.types.salesforce_data_transfer_api

    out: SalesforceDataTransferApiList = []
    for item in data:
        out.append(
            aws_sdk_appflow.types.salesforce_data_transfer_api.deserialize_json(item)
        )
    return out
