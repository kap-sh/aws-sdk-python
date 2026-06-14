"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeNFSFileSharesInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.file_share_arn_list


class DescribeNFSFileSharesInput(TypedDict):
    file_share_arn_list: (
        "aws_sdk_storage_gateway.types.file_share_arn_list.FileShareARNList"
    )
    """<p>An array containing the Amazon Resource Name (ARN) of each file share to be described.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeNFSFileSharesInput) -> dict:
    out: dict = {}
    import aws_sdk_storage_gateway.types.file_share_arn_list

    out["FileShareARNList"] = (
        aws_sdk_storage_gateway.types.file_share_arn_list.serialize_aws_json_1_1(
            value["file_share_arn_list"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeNFSFileSharesInput:
    out: DescribeNFSFileSharesInput = {}  # type: ignore[typeddict-item]
    if "FileShareARNList" in data:
        import aws_sdk_storage_gateway.types.file_share_arn_list

        out["file_share_arn_list"] = (
            aws_sdk_storage_gateway.types.file_share_arn_list.deserialize_aws_json_1_1(
                data["FileShareARNList"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeNFSFileSharesInput.file_share_arn_list required"
        )
    return out
