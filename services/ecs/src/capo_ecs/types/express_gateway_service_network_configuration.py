"""Generated from Smithy shape ``com.amazonaws.ecs#ExpressGatewayServiceNetworkConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string_list


class ExpressGatewayServiceNetworkConfiguration(TypedDict, closed=True):
    security_groups: NotRequired["capo_ecs.types.string_list.StringList"]
    """<p>The IDs of the security groups associated with the Express service.</p>"""
    subnets: NotRequired["capo_ecs.types.string_list.StringList"]
    """<p>The IDs of the subnets associated with the Express service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpressGatewayServiceNetworkConfiguration) -> dict:
    out: dict = {}
    if "security_groups" in value:
        import capo_ecs.types.string_list

        out["securityGroups"] = capo_ecs.types.string_list.serialize_aws_json_1_1(
            value["security_groups"]
        )
    if "subnets" in value:
        import capo_ecs.types.string_list

        out["subnets"] = capo_ecs.types.string_list.serialize_aws_json_1_1(
            value["subnets"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExpressGatewayServiceNetworkConfiguration:
    out: ExpressGatewayServiceNetworkConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("securityGroups") is not None:
        import capo_ecs.types.string_list

        out["security_groups"] = capo_ecs.types.string_list.deserialize_aws_json_1_1(
            data["securityGroups"]
        )
    if data.get("subnets") is not None:
        import capo_ecs.types.string_list

        out["subnets"] = capo_ecs.types.string_list.deserialize_aws_json_1_1(
            data["subnets"]
        )
    return out
