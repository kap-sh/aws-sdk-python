"""Generated from Smithy shape ``com.amazonaws.transfer#ConnectorFileTransferResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_transfer.types.connector_file_transfer_result

ConnectorFileTransferResults: TypeAlias = list[
    "aws_sdk_transfer.types.connector_file_transfer_result.ConnectorFileTransferResult"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectorFileTransferResults) -> list:
    import aws_sdk_transfer.types.connector_file_transfer_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_transfer.types.connector_file_transfer_result.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConnectorFileTransferResults:
    import aws_sdk_transfer.types.connector_file_transfer_result

    out: ConnectorFileTransferResults = []
    for item in data:
        out.append(
            aws_sdk_transfer.types.connector_file_transfer_result.deserialize_aws_json_1_1(
                item
            )
        )
    return out
