"""Generated from Smithy shape ``com.amazonaws.glacier#SetDataRetrievalPolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glacier.types.data_retrieval_policy
    import capo_glacier.types.string


class SetDataRetrievalPolicyInput(TypedDict, closed=True):
    account_id: "capo_glacier.types.string.string"
    """<p>The <code>AccountId</code> value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID.</p>"""
    policy: NotRequired["capo_glacier.types.data_retrieval_policy.DataRetrievalPolicy"]
    """<p>The data retrieval policy in JSON format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SetDataRetrievalPolicyInput) -> dict:
    out: dict = {}
    if "policy" in value:
        import capo_glacier.types.data_retrieval_policy

        out["Policy"] = capo_glacier.types.data_retrieval_policy.serialize_json(
            value["policy"]
        )
    return out


def deserialize_json(data: dict) -> SetDataRetrievalPolicyInput:
    out: SetDataRetrievalPolicyInput = {}  # type: ignore[typeddict-item]
    if "Policy" in data:
        import capo_glacier.types.data_retrieval_policy

        out["policy"] = capo_glacier.types.data_retrieval_policy.deserialize_json(
            data["Policy"]
        )
    return out
