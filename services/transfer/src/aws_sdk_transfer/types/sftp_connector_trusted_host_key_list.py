"""Generated from Smithy shape ``com.amazonaws.transfer#SftpConnectorTrustedHostKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_transfer.types.sftp_connector_trusted_host_key

SftpConnectorTrustedHostKeyList: TypeAlias = list[
    "aws_sdk_transfer.types.sftp_connector_trusted_host_key.SftpConnectorTrustedHostKey"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SftpConnectorTrustedHostKeyList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SftpConnectorTrustedHostKeyList:
    return list(data)
