"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#DeploySystemInstanceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotthingsgraph.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.greengrass_deployment_id
    import aws_sdk_iotthingsgraph.types.system_instance_summary


class DeploySystemInstanceResponse(TypedDict, closed=True):
    summary: (
        "aws_sdk_iotthingsgraph.types.system_instance_summary.SystemInstanceSummary"
    )
    """<p>An object that contains summary information about a system instance that was deployed. </p>"""
    greengrass_deployment_id: NotRequired[
        "aws_sdk_iotthingsgraph.types.greengrass_deployment_id.GreengrassDeploymentId"
    ]
    """<p>The ID of the Greengrass deployment used to deploy the system instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploySystemInstanceResponse) -> dict:
    out: dict = {}
    import aws_sdk_iotthingsgraph.types.system_instance_summary

    out["summary"] = (
        aws_sdk_iotthingsgraph.types.system_instance_summary.serialize_aws_json_1_1(
            value["summary"]
        )
    )
    if "greengrass_deployment_id" in value:
        out["greengrassDeploymentId"] = value["greengrass_deployment_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeploySystemInstanceResponse:
    out: DeploySystemInstanceResponse = {}  # type: ignore[typeddict-item]
    if "summary" in data:
        import aws_sdk_iotthingsgraph.types.system_instance_summary

        out["summary"] = (
            aws_sdk_iotthingsgraph.types.system_instance_summary.deserialize_aws_json_1_1(
                data["summary"]
            )
        )
    else:
        raise DeserializationError("DeploySystemInstanceResponse.summary required")
    if "greengrassDeploymentId" in data:
        out["greengrass_deployment_id"] = data["greengrassDeploymentId"]
    return out
