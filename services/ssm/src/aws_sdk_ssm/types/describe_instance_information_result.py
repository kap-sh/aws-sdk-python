"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeInstanceInformationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.instance_information_list
    import aws_sdk_ssm.types.next_token


class DescribeInstanceInformationResult(TypedDict, closed=True):
    instance_information_list: NotRequired[
        "aws_sdk_ssm.types.instance_information_list.InstanceInformationList"
    ]
    """<p>The managed node information list.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeInstanceInformationResult) -> dict:
    out: dict = {}
    if "instance_information_list" in value:
        import aws_sdk_ssm.types.instance_information_list

        out["InstanceInformationList"] = (
            aws_sdk_ssm.types.instance_information_list.serialize_aws_json_1_1(
                value["instance_information_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeInstanceInformationResult:
    out: DescribeInstanceInformationResult = {}  # type: ignore[typeddict-item]
    if "InstanceInformationList" in data:
        import aws_sdk_ssm.types.instance_information_list

        out["instance_information_list"] = (
            aws_sdk_ssm.types.instance_information_list.deserialize_aws_json_1_1(
                data["InstanceInformationList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
