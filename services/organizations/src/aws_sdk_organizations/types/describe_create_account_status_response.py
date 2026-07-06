"""Generated from Smithy shape ``com.amazonaws.organizations#DescribeCreateAccountStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_organizations.types.create_account_status


class DescribeCreateAccountStatusResponse(TypedDict, closed=True):
    create_account_status: NotRequired[
        "aws_sdk_organizations.types.create_account_status.CreateAccountStatus"
    ]
    """<p>A structure that contains the current status of an account creation request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCreateAccountStatusResponse) -> dict:
    out: dict = {}
    if "create_account_status" in value:
        import aws_sdk_organizations.types.create_account_status

        out["CreateAccountStatus"] = (
            aws_sdk_organizations.types.create_account_status.serialize_aws_json_1_1(
                value["create_account_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCreateAccountStatusResponse:
    out: DescribeCreateAccountStatusResponse = {}  # type: ignore[typeddict-item]
    if "CreateAccountStatus" in data:
        import aws_sdk_organizations.types.create_account_status

        out["create_account_status"] = (
            aws_sdk_organizations.types.create_account_status.deserialize_aws_json_1_1(
                data["CreateAccountStatus"]
            )
        )
    return out
