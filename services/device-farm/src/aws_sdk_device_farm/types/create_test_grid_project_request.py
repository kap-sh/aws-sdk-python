"""Generated from Smithy shape ``com.amazonaws.devicefarm#CreateTestGridProjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_device_farm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.resource_description
    import aws_sdk_device_farm.types.resource_name
    import aws_sdk_device_farm.types.test_grid_vpc_config


class CreateTestGridProjectRequest(TypedDict, closed=True):
    name: "aws_sdk_device_farm.types.resource_name.ResourceName"
    """<p>Human-readable name of the Selenium testing project.</p>"""
    description: NotRequired[
        "aws_sdk_device_farm.types.resource_description.ResourceDescription"
    ]
    """<p>Human-readable description of the project.</p>"""
    vpc_config: NotRequired[
        "aws_sdk_device_farm.types.test_grid_vpc_config.TestGridVpcConfig"
    ]
    """<p>The VPC security groups and subnets that are attached to a project.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTestGridProjectRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "vpc_config" in value:
        import aws_sdk_device_farm.types.test_grid_vpc_config

        out["vpcConfig"] = (
            aws_sdk_device_farm.types.test_grid_vpc_config.serialize_aws_json_1_1(
                value["vpc_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTestGridProjectRequest:
    out: CreateTestGridProjectRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateTestGridProjectRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "vpcConfig" in data:
        import aws_sdk_device_farm.types.test_grid_vpc_config

        out["vpc_config"] = (
            aws_sdk_device_farm.types.test_grid_vpc_config.deserialize_aws_json_1_1(
                data["vpcConfig"]
            )
        )
    return out
