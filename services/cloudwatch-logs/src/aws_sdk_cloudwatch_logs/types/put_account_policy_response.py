"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutAccountPolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.account_policy


class PutAccountPolicyResponse(TypedDict):
    account_policy: NotRequired[
        "aws_sdk_cloudwatch_logs.types.account_policy.AccountPolicy"
    ]
    """<p>The account policy that you created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutAccountPolicyResponse) -> dict:
    out: dict = {}
    if "account_policy" in value:
        import aws_sdk_cloudwatch_logs.types.account_policy

        out["accountPolicy"] = (
            aws_sdk_cloudwatch_logs.types.account_policy.serialize_aws_json_1_1(
                value["account_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutAccountPolicyResponse:
    out: PutAccountPolicyResponse = {}  # type: ignore[typeddict-item]
    if "accountPolicy" in data:
        import aws_sdk_cloudwatch_logs.types.account_policy

        out["account_policy"] = (
            aws_sdk_cloudwatch_logs.types.account_policy.deserialize_aws_json_1_1(
                data["accountPolicy"]
            )
        )
    return out
