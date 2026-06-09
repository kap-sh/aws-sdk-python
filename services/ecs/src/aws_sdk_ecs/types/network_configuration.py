"""Generated from Smithy shape ``com.amazonaws.ecs#NetworkConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.aws_vpc_configuration


class NetworkConfiguration(TypedDict):
    awsvpc_configuration: NotRequired[
        "aws_sdk_ecs.types.aws_vpc_configuration.AwsVpcConfiguration"
    ]
    """<p>The VPC subnets and security groups that are associated with a task.</p> <note> <p>All specified subnets and security groups must be from the same VPC.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkConfiguration) -> dict:
    out: dict = {}
    if "awsvpc_configuration" in value:
        import aws_sdk_ecs.types.aws_vpc_configuration

        out["awsvpcConfiguration"] = (
            aws_sdk_ecs.types.aws_vpc_configuration.serialize_aws_json_1_1(
                value["awsvpc_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> NetworkConfiguration:
    out: NetworkConfiguration = {}  # type: ignore[typeddict-item]
    if "awsvpcConfiguration" in data:
        import aws_sdk_ecs.types.aws_vpc_configuration

        out["awsvpc_configuration"] = (
            aws_sdk_ecs.types.aws_vpc_configuration.deserialize_aws_json_1_1(
                data["awsvpcConfiguration"]
            )
        )
    return out
