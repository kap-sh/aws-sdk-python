"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#ListTagsForResourceInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.amazon_resource_name


class ListTagsForResourceInput(TypedDict):
    resource_arn: (
        "aws_sdk_verifiedpermissions.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The ARN of the resource for which you want to view tags.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceInput) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceInput:
    out: ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("ListTagsForResourceInput.resource_arn required")
    return out
