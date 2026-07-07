"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeInstancePropertiesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.instance_properties
    import aws_sdk_ssm.types.next_token


class DescribeInstancePropertiesResult(TypedDict, closed=True):
    instance_properties: NotRequired[
        "aws_sdk_ssm.types.instance_properties.InstanceProperties"
    ]
    """<p>Properties for the managed instances.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of properties to return. Use this token to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeInstancePropertiesResult) -> dict:
    out: dict = {}
    if "instance_properties" in value:
        import aws_sdk_ssm.types.instance_properties

        out["InstanceProperties"] = (
            aws_sdk_ssm.types.instance_properties.serialize_aws_json_1_1(
                value["instance_properties"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeInstancePropertiesResult:
    out: DescribeInstancePropertiesResult = {}  # type: ignore[typeddict-item]
    if "InstanceProperties" in data:
        import aws_sdk_ssm.types.instance_properties

        out["instance_properties"] = (
            aws_sdk_ssm.types.instance_properties.deserialize_aws_json_1_1(
                data["InstanceProperties"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
