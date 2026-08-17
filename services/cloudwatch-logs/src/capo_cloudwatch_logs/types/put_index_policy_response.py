"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutIndexPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.index_policy


class PutIndexPolicyResponse(TypedDict, closed=True):
    index_policy: NotRequired["capo_cloudwatch_logs.types.index_policy.IndexPolicy"]
    """<p>The index policy that you just created or updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutIndexPolicyResponse) -> dict:
    out: dict = {}
    if "index_policy" in value:
        import capo_cloudwatch_logs.types.index_policy

        out["indexPolicy"] = (
            capo_cloudwatch_logs.types.index_policy.serialize_aws_json_1_1(
                value["index_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutIndexPolicyResponse:
    out: PutIndexPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("indexPolicy") is not None:
        import capo_cloudwatch_logs.types.index_policy

        out["index_policy"] = (
            capo_cloudwatch_logs.types.index_policy.deserialize_aws_json_1_1(
                data["indexPolicy"]
            )
        )
    return out
