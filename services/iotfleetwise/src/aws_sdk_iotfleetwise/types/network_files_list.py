"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#NetworkFilesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.network_file_blob

NetworkFilesList: TypeAlias = list[
    "aws_sdk_iotfleetwise.types.network_file_blob.NetworkFileBlob"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NetworkFilesList) -> list:
    import aws_sdk_iotfleetwise.types.network_file_blob

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotfleetwise.types.network_file_blob.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> NetworkFilesList:
    import aws_sdk_iotfleetwise.types.network_file_blob

    out: NetworkFilesList = []
    for item in data:
        out.append(
            aws_sdk_iotfleetwise.types.network_file_blob.deserialize_aws_json_1_0(item)
        )
    return out
