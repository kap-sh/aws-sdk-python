"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#ListAliasesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography.types.key_arn
    import aws_sdk_payment_cryptography.types.max_results
    import aws_sdk_payment_cryptography.types.next_token


class ListAliasesInput(TypedDict):
    key_arn: NotRequired["aws_sdk_payment_cryptography.types.key_arn.KeyArn"]
    """<p>The <code>keyARN</code> for which you want to list all aliases.</p>"""
    next_token: NotRequired["aws_sdk_payment_cryptography.types.next_token.NextToken"]
    """<p>Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of <code>NextToken</code> from the truncated response you just received.</p>"""
    max_results: NotRequired[
        "aws_sdk_payment_cryptography.types.max_results.MaxResults"
    ]
    """<p>Use this parameter to specify the maximum number of items to return. When this value is present, Amazon Web Services Payment Cryptography does not return more than the specified number of items, but it might return fewer.</p> <p>This value is optional. If you include a value, it must be between 1 and 100, inclusive. If you do not include a value, it defaults to 50.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAliasesInput) -> dict:
    out: dict = {}
    if "key_arn" in value:
        out["KeyArn"] = value["key_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAliasesInput:
    out: ListAliasesInput = {}  # type: ignore[typeddict-item]
    if "KeyArn" in data:
        out["key_arn"] = data["KeyArn"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
