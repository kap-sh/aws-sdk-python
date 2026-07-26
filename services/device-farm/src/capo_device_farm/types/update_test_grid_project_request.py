"""Generated from Smithy shape ``com.amazonaws.devicefarm#UpdateTestGridProjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_device_farm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_device_farm.types.device_farm_arn
    import capo_device_farm.types.resource_description
    import capo_device_farm.types.resource_name
    import capo_device_farm.types.test_grid_vpc_config


class UpdateTestGridProjectRequest(TypedDict, closed=True):
    project_arn: "capo_device_farm.types.device_farm_arn.DeviceFarmArn"
    """<p>ARN of the project to update.</p>"""
    name: NotRequired["capo_device_farm.types.resource_name.ResourceName"]
    """<p>Human-readable name for the project.</p>"""
    description: NotRequired[
        "capo_device_farm.types.resource_description.ResourceDescription"
    ]
    """<p>Human-readable description for the project.</p>"""
    vpc_config: NotRequired[
        "capo_device_farm.types.test_grid_vpc_config.TestGridVpcConfig"
    ]
    """<p>The VPC security groups and subnets that are attached to a project.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTestGridProjectRequest) -> dict:
    out: dict = {}
    out["projectArn"] = value["project_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "vpc_config" in value:
        import capo_device_farm.types.test_grid_vpc_config

        out["vpcConfig"] = (
            capo_device_farm.types.test_grid_vpc_config.serialize_aws_json_1_1(
                value["vpc_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTestGridProjectRequest:
    out: UpdateTestGridProjectRequest = {}  # type: ignore[typeddict-item]
    if "projectArn" in data:
        out["project_arn"] = data["projectArn"]
    else:
        raise DeserializationError("UpdateTestGridProjectRequest.project_arn required")
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "vpcConfig" in data:
        import capo_device_farm.types.test_grid_vpc_config

        out["vpc_config"] = (
            capo_device_farm.types.test_grid_vpc_config.deserialize_aws_json_1_1(
                data["vpcConfig"]
            )
        )
    return out
