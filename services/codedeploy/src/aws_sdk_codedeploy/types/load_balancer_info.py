"""Generated from Smithy shape ``com.amazonaws.codedeploy#LoadBalancerInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.elb_info_list
    import aws_sdk_codedeploy.types.target_group_info_list
    import aws_sdk_codedeploy.types.target_group_pair_info_list


class LoadBalancerInfo(TypedDict, closed=True):
    elb_info_list: NotRequired["aws_sdk_codedeploy.types.elb_info_list.ELBInfoList"]
    """<p>An array that contains information about the load balancers to use for load balancing in a deployment. If you're using Classic Load Balancers, specify those load balancers in this array. </p> <note> <p>You can add up to 10 load balancers to the array.</p> </note> <note> <p>If you're using Application Load Balancers or Network Load Balancers, use the <code>targetGroupInfoList</code> array instead of this one.</p> </note>"""
    target_group_info_list: NotRequired[
        "aws_sdk_codedeploy.types.target_group_info_list.TargetGroupInfoList"
    ]
    """<p>An array that contains information about the target groups to use for load balancing in a deployment. If you're using Application Load Balancers and Network Load Balancers, specify their associated target groups in this array.</p> <note> <p>You can add up to 10 target groups to the array.</p> </note> <note> <p>If you're using Classic Load Balancers, use the <code>elbInfoList</code> array instead of this one.</p> </note>"""
    target_group_pair_info_list: NotRequired[
        "aws_sdk_codedeploy.types.target_group_pair_info_list.TargetGroupPairInfoList"
    ]
    """<p> The target group pair information. This is an array of <code>TargeGroupPairInfo</code> objects with a maximum size of one. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoadBalancerInfo) -> dict:
    out: dict = {}
    if "elb_info_list" in value:
        import aws_sdk_codedeploy.types.elb_info_list

        out["elbInfoList"] = (
            aws_sdk_codedeploy.types.elb_info_list.serialize_aws_json_1_1(
                value["elb_info_list"]
            )
        )
    if "target_group_info_list" in value:
        import aws_sdk_codedeploy.types.target_group_info_list

        out["targetGroupInfoList"] = (
            aws_sdk_codedeploy.types.target_group_info_list.serialize_aws_json_1_1(
                value["target_group_info_list"]
            )
        )
    if "target_group_pair_info_list" in value:
        import aws_sdk_codedeploy.types.target_group_pair_info_list

        out["targetGroupPairInfoList"] = (
            aws_sdk_codedeploy.types.target_group_pair_info_list.serialize_aws_json_1_1(
                value["target_group_pair_info_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LoadBalancerInfo:
    out: LoadBalancerInfo = {}  # type: ignore[typeddict-item]
    if "elbInfoList" in data:
        import aws_sdk_codedeploy.types.elb_info_list

        out["elb_info_list"] = (
            aws_sdk_codedeploy.types.elb_info_list.deserialize_aws_json_1_1(
                data["elbInfoList"]
            )
        )
    if "targetGroupInfoList" in data:
        import aws_sdk_codedeploy.types.target_group_info_list

        out["target_group_info_list"] = (
            aws_sdk_codedeploy.types.target_group_info_list.deserialize_aws_json_1_1(
                data["targetGroupInfoList"]
            )
        )
    if "targetGroupPairInfoList" in data:
        import aws_sdk_codedeploy.types.target_group_pair_info_list

        out["target_group_pair_info_list"] = (
            aws_sdk_codedeploy.types.target_group_pair_info_list.deserialize_aws_json_1_1(
                data["targetGroupPairInfoList"]
            )
        )
    return out
