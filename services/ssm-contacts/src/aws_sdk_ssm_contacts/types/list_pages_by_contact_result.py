"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ListPagesByContactResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.pages_list
    import aws_sdk_ssm_contacts.types.pagination_token


class ListPagesByContactResult(TypedDict, closed=True):
    next_token: NotRequired[
        "aws_sdk_ssm_contacts.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token to continue to the next page of results.</p>"""
    pages: "aws_sdk_ssm_contacts.types.pages_list.PagesList"
    """<p>The list of engagements to a contact's contact channel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPagesByContactResult) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import aws_sdk_ssm_contacts.types.pages_list

    out["Pages"] = aws_sdk_ssm_contacts.types.pages_list.serialize_aws_json_1_1(
        value["pages"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPagesByContactResult:
    out: ListPagesByContactResult = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Pages" in data:
        import aws_sdk_ssm_contacts.types.pages_list

        out["pages"] = aws_sdk_ssm_contacts.types.pages_list.deserialize_aws_json_1_1(
            data["Pages"]
        )
    else:
        raise DeserializationError("ListPagesByContactResult.pages required")
    return out
