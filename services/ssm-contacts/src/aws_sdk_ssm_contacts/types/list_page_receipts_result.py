"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ListPageReceiptsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.pagination_token
    import aws_sdk_ssm_contacts.types.receipts_list


class ListPageReceiptsResult(TypedDict, closed=True):
    next_token: NotRequired[
        "aws_sdk_ssm_contacts.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token to continue to the next page of results.</p>"""
    receipts: NotRequired["aws_sdk_ssm_contacts.types.receipts_list.ReceiptsList"]
    """<p>A list of each acknowledgement.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPageReceiptsResult) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "receipts" in value:
        import aws_sdk_ssm_contacts.types.receipts_list

        out["Receipts"] = (
            aws_sdk_ssm_contacts.types.receipts_list.serialize_aws_json_1_1(
                value["receipts"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPageReceiptsResult:
    out: ListPageReceiptsResult = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Receipts" in data:
        import aws_sdk_ssm_contacts.types.receipts_list

        out["receipts"] = (
            aws_sdk_ssm_contacts.types.receipts_list.deserialize_aws_json_1_1(
                data["Receipts"]
            )
        )
    return out
