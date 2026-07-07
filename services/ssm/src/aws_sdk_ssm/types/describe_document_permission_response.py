"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeDocumentPermissionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.account_id_list
    import aws_sdk_ssm.types.account_sharing_info_list
    import aws_sdk_ssm.types.next_token


class DescribeDocumentPermissionResponse(TypedDict, closed=True):
    account_ids: NotRequired["aws_sdk_ssm.types.account_id_list.AccountIdList"]
    """<p>The account IDs that have permission to use this document. The ID can be either an Amazon Web Services account number or <code>all</code>.</p>"""
    account_sharing_info_list: NotRequired[
        "aws_sdk_ssm.types.account_sharing_info_list.AccountSharingInfoList"
    ]
    """<p>A list of Amazon Web Services accounts where the current document is shared and the version shared with each account.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. Use this token to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDocumentPermissionResponse) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import aws_sdk_ssm.types.account_id_list

        out["AccountIds"] = aws_sdk_ssm.types.account_id_list.serialize_aws_json_1_1(
            value["account_ids"]
        )
    if "account_sharing_info_list" in value:
        import aws_sdk_ssm.types.account_sharing_info_list

        out["AccountSharingInfoList"] = (
            aws_sdk_ssm.types.account_sharing_info_list.serialize_aws_json_1_1(
                value["account_sharing_info_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDocumentPermissionResponse:
    out: DescribeDocumentPermissionResponse = {}  # type: ignore[typeddict-item]
    if "AccountIds" in data:
        import aws_sdk_ssm.types.account_id_list

        out["account_ids"] = aws_sdk_ssm.types.account_id_list.deserialize_aws_json_1_1(
            data["AccountIds"]
        )
    if "AccountSharingInfoList" in data:
        import aws_sdk_ssm.types.account_sharing_info_list

        out["account_sharing_info_list"] = (
            aws_sdk_ssm.types.account_sharing_info_list.deserialize_aws_json_1_1(
                data["AccountSharingInfoList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
