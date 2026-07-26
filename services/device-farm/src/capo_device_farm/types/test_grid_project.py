"""Generated from Smithy shape ``com.amazonaws.devicefarm#TestGridProject``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.date_time
    import capo_device_farm.types.device_farm_arn
    import capo_device_farm.types.string
    import capo_device_farm.types.test_grid_vpc_config


class TestGridProject(TypedDict, closed=True):
    arn: NotRequired["capo_device_farm.types.device_farm_arn.DeviceFarmArn"]
    """<p>The ARN for the project.</p>"""
    name: NotRequired["capo_device_farm.types.string.String"]
    """<p>A human-readable name for the project.</p>"""
    description: NotRequired["capo_device_farm.types.string.String"]
    """<p>A human-readable description for the project.</p>"""
    vpc_config: NotRequired[
        "capo_device_farm.types.test_grid_vpc_config.TestGridVpcConfig"
    ]
    """<p>The VPC security groups and subnets that are attached to a project.</p>"""
    created: NotRequired["capo_device_farm.types.date_time.DateTime"]
    """<p>When the project was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestGridProject) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
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
    if "created" in value:
        import capo_device_farm.types.date_time

        out["created"] = capo_device_farm.types.date_time.serialize_aws_json_1_1(
            value["created"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TestGridProject:
    out: TestGridProject = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
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
    if "created" in data:
        import capo_device_farm.types.date_time

        out["created"] = capo_device_farm.types.date_time.deserialize_aws_json_1_1(
            data["created"]
        )
    return out
