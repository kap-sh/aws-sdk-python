"""Generated from Smithy shape ``com.amazonaws.glacier#GetDataRetrievalPolicyOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glacier.types.data_retrieval_policy


class GetDataRetrievalPolicyOutput(TypedDict, closed=True):
    policy: NotRequired[
        "aws_sdk_glacier.types.data_retrieval_policy.DataRetrievalPolicy"
    ]
    """<p>Contains the returned data retrieval policy in JSON format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataRetrievalPolicyOutput) -> dict:
    out: dict = {}
    if "policy" in value:
        import aws_sdk_glacier.types.data_retrieval_policy

        out["Policy"] = aws_sdk_glacier.types.data_retrieval_policy.serialize_json(
            value["policy"]
        )
    return out


def deserialize_json(data: dict) -> GetDataRetrievalPolicyOutput:
    out: GetDataRetrievalPolicyOutput = {}  # type: ignore[typeddict-item]
    if "Policy" in data:
        import aws_sdk_glacier.types.data_retrieval_policy

        out["policy"] = aws_sdk_glacier.types.data_retrieval_policy.deserialize_json(
            data["Policy"]
        )
    return out
