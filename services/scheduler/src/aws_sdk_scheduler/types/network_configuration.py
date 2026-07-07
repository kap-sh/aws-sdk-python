"""Generated from Smithy shape ``com.amazonaws.scheduler#NetworkConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_scheduler.types.aws_vpc_configuration


class NetworkConfiguration(TypedDict, closed=True):
    awsvpc_configuration: NotRequired[
        "aws_sdk_scheduler.types.aws_vpc_configuration.AwsVpcConfiguration"
    ]
    """<p>Specifies the Amazon VPC subnets and security groups for the task, and whether a public IP address is to be used. This structure is relevant only for ECS tasks that use the awsvpc network mode.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkConfiguration) -> dict:
    out: dict = {}
    if "awsvpc_configuration" in value:
        import aws_sdk_scheduler.types.aws_vpc_configuration

        out["awsvpcConfiguration"] = (
            aws_sdk_scheduler.types.aws_vpc_configuration.serialize_json(
                value["awsvpc_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> NetworkConfiguration:
    out: NetworkConfiguration = {}  # type: ignore[typeddict-item]
    if "awsvpcConfiguration" in data:
        import aws_sdk_scheduler.types.aws_vpc_configuration

        out["awsvpc_configuration"] = (
            aws_sdk_scheduler.types.aws_vpc_configuration.deserialize_json(
                data["awsvpcConfiguration"]
            )
        )
    return out
