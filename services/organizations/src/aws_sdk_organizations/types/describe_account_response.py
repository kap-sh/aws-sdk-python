"""Generated from Smithy shape ``com.amazonaws.organizations#DescribeAccountResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_organizations.types.account


class DescribeAccountResponse(TypedDict):
    account: NotRequired["aws_sdk_organizations.types.account.Account"]
    """<p>A structure that contains information about the requested account.</p> <important> <p>The <code>Status</code> parameter in the API response will be retired on September 9, 2026. Although both the account <code>State</code> and account <code>Status</code> parameters are currently available in the Organizations APIs (<code>DescribeAccount</code>, <code>ListAccounts</code>, <code>ListAccountsForParent</code>), we recommend that you update your scripts or other code to use the <code>State</code> parameter instead of <code>Status</code> before September 9, 2026.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAccountResponse) -> dict:
    out: dict = {}
    if "account" in value:
        import aws_sdk_organizations.types.account

        out["Account"] = aws_sdk_organizations.types.account.serialize_aws_json_1_1(
            value["account"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAccountResponse:
    out: DescribeAccountResponse = {}  # type: ignore[typeddict-item]
    if "Account" in data:
        import aws_sdk_organizations.types.account

        out["account"] = aws_sdk_organizations.types.account.deserialize_aws_json_1_1(
            data["Account"]
        )
    return out
