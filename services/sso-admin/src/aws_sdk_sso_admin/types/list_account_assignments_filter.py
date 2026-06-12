"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListAccountAssignmentsFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.account_id


class ListAccountAssignmentsFilter(TypedDict):
    account_id: NotRequired["aws_sdk_sso_admin.types.account_id.AccountId"]
    """<p>The ID number of an Amazon Web Services account that filters the results in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAccountAssignmentsFilter) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAccountAssignmentsFilter:
    out: ListAccountAssignmentsFilter = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    return out
