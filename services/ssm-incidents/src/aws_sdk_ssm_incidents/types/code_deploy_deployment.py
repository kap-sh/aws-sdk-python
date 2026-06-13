"""Generated from Smithy shape ``com.amazonaws.ssmincidents#CodeDeployDeployment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_ssm_incidents.types.arn


class CodeDeployDeployment(TypedDict):
    start_time: "datetime.datetime"
    """<p>The timestamp for when the CodeDeploy deployment began.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The timestamp for when the CodeDeploy deployment ended. Not reported for deployments that are still in progress.</p>"""
    deployment_group_arn: "aws_sdk_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the CodeDeploy deployment group associated with the deployment.</p>"""
    deployment_id: "str"
    """<p>The ID of the CodeDeploy deployment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeDeployDeployment) -> dict:
    out: dict = {}
    import aws_sdk_ssm_incidents.types._prelude.timestamp

    out["startTime"] = aws_sdk_ssm_incidents.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    if "end_time" in value:
        import aws_sdk_ssm_incidents.types._prelude.timestamp

        out["endTime"] = aws_sdk_ssm_incidents.types._prelude.timestamp.serialize_json(
            value["end_time"]
        )
    out["deploymentGroupArn"] = value["deployment_group_arn"]
    out["deploymentId"] = value["deployment_id"]
    return out


def deserialize_json(data: dict) -> CodeDeployDeployment:
    out: CodeDeployDeployment = {}  # type: ignore[typeddict-item]
    if "startTime" in data:
        import aws_sdk_ssm_incidents.types._prelude.timestamp

        out["start_time"] = (
            aws_sdk_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["startTime"]
            )
        )
    else:
        raise DeserializationError("CodeDeployDeployment.start_time required")
    if "endTime" in data:
        import aws_sdk_ssm_incidents.types._prelude.timestamp

        out["end_time"] = (
            aws_sdk_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["endTime"]
            )
        )
    if "deploymentGroupArn" in data:
        out["deployment_group_arn"] = data["deploymentGroupArn"]
    else:
        raise DeserializationError("CodeDeployDeployment.deployment_group_arn required")
    if "deploymentId" in data:
        out["deployment_id"] = data["deploymentId"]
    else:
        raise DeserializationError("CodeDeployDeployment.deployment_id required")
    return out
