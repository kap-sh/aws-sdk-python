"""Generated from Smithy shape ``com.amazonaws.inspector#DescribeResourceGroupsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.batch_describe_arn_list


class DescribeResourceGroupsRequest(TypedDict):
    resource_group_arns: (
        "aws_sdk_inspector.types.batch_describe_arn_list.BatchDescribeArnList"
    )
    """<p>The ARN that specifies the resource group that you want to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeResourceGroupsRequest) -> dict:
    out: dict = {}
    import aws_sdk_inspector.types.batch_describe_arn_list

    out["resourceGroupArns"] = (
        aws_sdk_inspector.types.batch_describe_arn_list.serialize_aws_json_1_1(
            value["resource_group_arns"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeResourceGroupsRequest:
    out: DescribeResourceGroupsRequest = {}  # type: ignore[typeddict-item]
    if "resourceGroupArns" in data:
        import aws_sdk_inspector.types.batch_describe_arn_list

        out["resource_group_arns"] = (
            aws_sdk_inspector.types.batch_describe_arn_list.deserialize_aws_json_1_1(
                data["resourceGroupArns"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeResourceGroupsRequest.resource_group_arns required"
        )
    return out
