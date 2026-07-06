"""Generated from Smithy shape ``com.amazonaws.codedeploy#BatchGetDeploymentsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.deployments_info_list


class BatchGetDeploymentsOutput(TypedDict, closed=True):
    deployments_info: NotRequired[
        "aws_sdk_codedeploy.types.deployments_info_list.DeploymentsInfoList"
    ]
    """<p> Information about the deployments. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetDeploymentsOutput) -> dict:
    out: dict = {}
    if "deployments_info" in value:
        import aws_sdk_codedeploy.types.deployments_info_list

        out["deploymentsInfo"] = (
            aws_sdk_codedeploy.types.deployments_info_list.serialize_aws_json_1_1(
                value["deployments_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetDeploymentsOutput:
    out: BatchGetDeploymentsOutput = {}  # type: ignore[typeddict-item]
    if "deploymentsInfo" in data:
        import aws_sdk_codedeploy.types.deployments_info_list

        out["deployments_info"] = (
            aws_sdk_codedeploy.types.deployments_info_list.deserialize_aws_json_1_1(
                data["deploymentsInfo"]
            )
        )
    return out
