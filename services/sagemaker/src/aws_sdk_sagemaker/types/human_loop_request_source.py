"""Generated from Smithy shape ``com.amazonaws.sagemaker#HumanLoopRequestSource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.aws_managed_human_loop_request_source


class HumanLoopRequestSource(TypedDict):
    aws_managed_human_loop_request_source: NotRequired[
        "aws_sdk_sagemaker.types.aws_managed_human_loop_request_source.AwsManagedHumanLoopRequestSource"
    ]
    """<p>Specifies whether Amazon Rekognition or Amazon Textract are used as the integration source. The default field settings and JSON parsing rules are different based on the integration source. Valid values:</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HumanLoopRequestSource) -> dict:
    out: dict = {}
    if "aws_managed_human_loop_request_source" in value:
        import aws_sdk_sagemaker.types.aws_managed_human_loop_request_source

        out["AwsManagedHumanLoopRequestSource"] = (
            aws_sdk_sagemaker.types.aws_managed_human_loop_request_source.serialize_aws_json_1_1(
                value["aws_managed_human_loop_request_source"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HumanLoopRequestSource:
    out: HumanLoopRequestSource = {}  # type: ignore[typeddict-item]
    if "AwsManagedHumanLoopRequestSource" in data:
        import aws_sdk_sagemaker.types.aws_managed_human_loop_request_source

        out["aws_managed_human_loop_request_source"] = (
            aws_sdk_sagemaker.types.aws_managed_human_loop_request_source.deserialize_aws_json_1_1(
                data["AwsManagedHumanLoopRequestSource"]
            )
        )
    return out
