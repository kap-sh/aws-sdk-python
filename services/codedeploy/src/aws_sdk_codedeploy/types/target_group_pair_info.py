"""Generated from Smithy shape ``com.amazonaws.codedeploy#TargetGroupPairInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.target_group_info_list
    import aws_sdk_codedeploy.types.traffic_route


class TargetGroupPairInfo(TypedDict):
    target_groups: NotRequired[
        "aws_sdk_codedeploy.types.target_group_info_list.TargetGroupInfoList"
    ]
    """<p> One pair of target groups. One is associated with the original task set. The second is associated with the task set that serves traffic after the deployment is complete. </p>"""
    prod_traffic_route: NotRequired[
        "aws_sdk_codedeploy.types.traffic_route.TrafficRoute"
    ]
    """<p> The path used by a load balancer to route production traffic when an Amazon ECS deployment is complete. </p>"""
    test_traffic_route: NotRequired[
        "aws_sdk_codedeploy.types.traffic_route.TrafficRoute"
    ]
    """<p> An optional path used by a load balancer to route test traffic after an Amazon ECS deployment. Validation can occur while test traffic is served during a deployment. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetGroupPairInfo) -> dict:
    out: dict = {}
    if "target_groups" in value:
        import aws_sdk_codedeploy.types.target_group_info_list

        out["targetGroups"] = (
            aws_sdk_codedeploy.types.target_group_info_list.serialize_aws_json_1_1(
                value["target_groups"]
            )
        )
    if "prod_traffic_route" in value:
        import aws_sdk_codedeploy.types.traffic_route

        out["prodTrafficRoute"] = (
            aws_sdk_codedeploy.types.traffic_route.serialize_aws_json_1_1(
                value["prod_traffic_route"]
            )
        )
    if "test_traffic_route" in value:
        import aws_sdk_codedeploy.types.traffic_route

        out["testTrafficRoute"] = (
            aws_sdk_codedeploy.types.traffic_route.serialize_aws_json_1_1(
                value["test_traffic_route"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetGroupPairInfo:
    out: TargetGroupPairInfo = {}  # type: ignore[typeddict-item]
    if "targetGroups" in data:
        import aws_sdk_codedeploy.types.target_group_info_list

        out["target_groups"] = (
            aws_sdk_codedeploy.types.target_group_info_list.deserialize_aws_json_1_1(
                data["targetGroups"]
            )
        )
    if "prodTrafficRoute" in data:
        import aws_sdk_codedeploy.types.traffic_route

        out["prod_traffic_route"] = (
            aws_sdk_codedeploy.types.traffic_route.deserialize_aws_json_1_1(
                data["prodTrafficRoute"]
            )
        )
    if "testTrafficRoute" in data:
        import aws_sdk_codedeploy.types.traffic_route

        out["test_traffic_route"] = (
            aws_sdk_codedeploy.types.traffic_route.deserialize_aws_json_1_1(
                data["testTrafficRoute"]
            )
        )
    return out
