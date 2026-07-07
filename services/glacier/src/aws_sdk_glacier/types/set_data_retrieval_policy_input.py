"""Generated from Smithy shape ``com.amazonaws.glacier#SetDataRetrievalPolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glacier.types.data_retrieval_policy
    import aws_sdk_glacier.types.string


class SetDataRetrievalPolicyInput(TypedDict, closed=True):
    account_id: "aws_sdk_glacier.types.string.string"
    """<p>The <code>AccountId</code> value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID.</p>"""
    policy: NotRequired[
        "aws_sdk_glacier.types.data_retrieval_policy.DataRetrievalPolicy"
    ]
    """<p>The data retrieval policy in JSON format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SetDataRetrievalPolicyInput) -> dict:
    out: dict = {}
    if "policy" in value:
        import aws_sdk_glacier.types.data_retrieval_policy

        out["Policy"] = aws_sdk_glacier.types.data_retrieval_policy.serialize_json(
            value["policy"]
        )
    return out


def deserialize_json(data: dict) -> SetDataRetrievalPolicyInput:
    out: SetDataRetrievalPolicyInput = {}  # type: ignore[typeddict-item]
    if "Policy" in data:
        import aws_sdk_glacier.types.data_retrieval_policy

        out["policy"] = aws_sdk_glacier.types.data_retrieval_policy.deserialize_json(
            data["Policy"]
        )
    return out
