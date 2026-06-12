"""Generated from Smithy shape ``com.amazonaws.ssm#GetPatchBaselineRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.baseline_id


class GetPatchBaselineRequest(TypedDict):
    baseline_id: "aws_sdk_ssm.types.baseline_id.BaselineId"
    """<p>The ID of the patch baseline to retrieve.</p> <note> <p>To retrieve information about an Amazon Web Services managed patch baseline, specify the full Amazon Resource Name (ARN) of the baseline. For example, for the baseline <code>AWS-AmazonLinuxDefaultPatchBaseline</code>, specify <code>arn:aws:ssm:us-east-2:733109147000:patchbaseline/pb-0e392de35e7c563b7</code> instead of <code>pb-0e392de35e7c563b7</code>.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPatchBaselineRequest) -> dict:
    out: dict = {}
    out["BaselineId"] = value["baseline_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPatchBaselineRequest:
    out: GetPatchBaselineRequest = {}  # type: ignore[typeddict-item]
    if "BaselineId" in data:
        out["baseline_id"] = data["BaselineId"]
    else:
        raise DeserializationError("GetPatchBaselineRequest.baseline_id required")
    return out
