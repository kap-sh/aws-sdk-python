"""Generated from Smithy shape ``com.amazonaws.directconnect#DescribeTagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.resource_arn_list


class DescribeTagsRequest(TypedDict, closed=True):
    resource_arns: "aws_sdk_direct_connect.types.resource_arn_list.ResourceArnList"
    """<p>The Amazon Resource Names (ARNs) of the resources.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTagsRequest) -> dict:
    out: dict = {}
    import aws_sdk_direct_connect.types.resource_arn_list

    out["resourceArns"] = (
        aws_sdk_direct_connect.types.resource_arn_list.serialize_aws_json_1_1(
            value["resource_arns"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTagsRequest:
    out: DescribeTagsRequest = {}  # type: ignore[typeddict-item]
    if "resourceArns" in data:
        import aws_sdk_direct_connect.types.resource_arn_list

        out["resource_arns"] = (
            aws_sdk_direct_connect.types.resource_arn_list.deserialize_aws_json_1_1(
                data["resourceArns"]
            )
        )
    else:
        raise DeserializationError("DescribeTagsRequest.resource_arns required")
    return out
