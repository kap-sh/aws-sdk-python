"""Generated from Smithy shape ``com.amazonaws.ecs#ExpressGatewayServiceNetworkConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string_list


class ExpressGatewayServiceNetworkConfiguration(TypedDict, closed=True):
    security_groups: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>The IDs of the security groups associated with the Express service.</p>"""
    subnets: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>The IDs of the subnets associated with the Express service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpressGatewayServiceNetworkConfiguration) -> dict:
    out: dict = {}
    if "security_groups" in value:
        import aws_sdk_ecs.types.string_list

        out["securityGroups"] = aws_sdk_ecs.types.string_list.serialize_aws_json_1_1(
            value["security_groups"]
        )
    if "subnets" in value:
        import aws_sdk_ecs.types.string_list

        out["subnets"] = aws_sdk_ecs.types.string_list.serialize_aws_json_1_1(
            value["subnets"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExpressGatewayServiceNetworkConfiguration:
    out: ExpressGatewayServiceNetworkConfiguration = {}  # type: ignore[typeddict-item]
    if "securityGroups" in data:
        import aws_sdk_ecs.types.string_list

        out["security_groups"] = aws_sdk_ecs.types.string_list.deserialize_aws_json_1_1(
            data["securityGroups"]
        )
    if "subnets" in data:
        import aws_sdk_ecs.types.string_list

        out["subnets"] = aws_sdk_ecs.types.string_list.deserialize_aws_json_1_1(
            data["subnets"]
        )
    return out
