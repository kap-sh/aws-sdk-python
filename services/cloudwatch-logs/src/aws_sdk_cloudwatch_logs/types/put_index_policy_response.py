"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutIndexPolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.index_policy


class PutIndexPolicyResponse(TypedDict):
    index_policy: NotRequired["aws_sdk_cloudwatch_logs.types.index_policy.IndexPolicy"]
    """<p>The index policy that you just created or updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutIndexPolicyResponse) -> dict:
    out: dict = {}
    if "index_policy" in value:
        import aws_sdk_cloudwatch_logs.types.index_policy

        out["indexPolicy"] = (
            aws_sdk_cloudwatch_logs.types.index_policy.serialize_aws_json_1_1(
                value["index_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutIndexPolicyResponse:
    out: PutIndexPolicyResponse = {}  # type: ignore[typeddict-item]
    if "indexPolicy" in data:
        import aws_sdk_cloudwatch_logs.types.index_policy

        out["index_policy"] = (
            aws_sdk_cloudwatch_logs.types.index_policy.deserialize_aws_json_1_1(
                data["indexPolicy"]
            )
        )
    return out
