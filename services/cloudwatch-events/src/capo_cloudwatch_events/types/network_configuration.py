"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#NetworkConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.aws_vpc_configuration


class NetworkConfiguration(TypedDict, closed=True):
    awsvpc_configuration: NotRequired[
        "capo_cloudwatch_events.types.aws_vpc_configuration.AwsVpcConfiguration"
    ]
    """<p>Use this structure to specify the VPC subnets and security groups for the task, and whether a public IP address is to be used. This structure is relevant only for ECS tasks that use the <code>awsvpc</code> network mode.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkConfiguration) -> dict:
    out: dict = {}
    if "awsvpc_configuration" in value:
        import capo_cloudwatch_events.types.aws_vpc_configuration

        out["awsvpcConfiguration"] = (
            capo_cloudwatch_events.types.aws_vpc_configuration.serialize_aws_json_1_1(
                value["awsvpc_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> NetworkConfiguration:
    out: NetworkConfiguration = {}  # type: ignore[typeddict-item]
    if "awsvpcConfiguration" in data:
        import capo_cloudwatch_events.types.aws_vpc_configuration

        out["awsvpc_configuration"] = (
            capo_cloudwatch_events.types.aws_vpc_configuration.deserialize_aws_json_1_1(
                data["awsvpcConfiguration"]
            )
        )
    return out
