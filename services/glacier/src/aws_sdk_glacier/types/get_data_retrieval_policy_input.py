"""Generated from Smithy shape ``com.amazonaws.glacier#GetDataRetrievalPolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_glacier.types.string


class GetDataRetrievalPolicyInput(TypedDict, closed=True):
    account_id: "aws_sdk_glacier.types.string.string"
    """<p>The <code>AccountId</code> value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataRetrievalPolicyInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDataRetrievalPolicyInput:
    out: GetDataRetrievalPolicyInput = {}  # type: ignore[typeddict-item]
    return out
