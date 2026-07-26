"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeSMBFileSharesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.smb_file_share_info_list


class DescribeSMBFileSharesOutput(TypedDict, closed=True):
    smb_file_share_info_list: NotRequired[
        "capo_storage_gateway.types.smb_file_share_info_list.SMBFileShareInfoList"
    ]
    """<p>An array containing a description for each requested file share.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSMBFileSharesOutput) -> dict:
    out: dict = {}
    if "smb_file_share_info_list" in value:
        import capo_storage_gateway.types.smb_file_share_info_list

        out["SMBFileShareInfoList"] = (
            capo_storage_gateway.types.smb_file_share_info_list.serialize_aws_json_1_1(
                value["smb_file_share_info_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSMBFileSharesOutput:
    out: DescribeSMBFileSharesOutput = {}  # type: ignore[typeddict-item]
    if "SMBFileShareInfoList" in data:
        import capo_storage_gateway.types.smb_file_share_info_list

        out["smb_file_share_info_list"] = (
            capo_storage_gateway.types.smb_file_share_info_list.deserialize_aws_json_1_1(
                data["SMBFileShareInfoList"]
            )
        )
    return out
