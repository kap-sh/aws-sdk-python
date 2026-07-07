"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#ListTagsForResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography.types.max_results
    import aws_sdk_payment_cryptography.types.next_token
    import aws_sdk_payment_cryptography.types.resource_arn


class ListTagsForResourceInput(TypedDict, closed=True):
    resource_arn: "aws_sdk_payment_cryptography.types.resource_arn.ResourceArn"
    """<p>The <code>KeyARN</code> of the key whose tags you are getting.</p>"""
    next_token: NotRequired["aws_sdk_payment_cryptography.types.next_token.NextToken"]
    """<p>Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of <code>NextToken</code> from the truncated response you just received.</p>"""
    max_results: NotRequired[
        "aws_sdk_payment_cryptography.types.max_results.MaxResults"
    ]
    """<p>Use this parameter to specify the maximum number of items to return. When this value is present, Amazon Web Services Payment Cryptography does not return more than the specified number of items, but it might return fewer.</p> <p>This value is optional. If you include a value, it must be between 1 and 100, inclusive. If you do not include a value, it defaults to 50.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceInput) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceInput:
    out: ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("ListTagsForResourceInput.resource_arn required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
