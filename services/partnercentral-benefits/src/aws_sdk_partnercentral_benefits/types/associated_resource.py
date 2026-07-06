"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#AssociatedResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_partnercentral_benefits.types.arn
    import aws_sdk_partnercentral_benefits.types.resource_type


class AssociatedResource(TypedDict, closed=True):
    resource_type: NotRequired[
        "aws_sdk_partnercentral_benefits.types.resource_type.ResourceType"
    ]
    """<p>The type of AWS resource (e.g., EC2 instance, S3 bucket, Lambda function).</p>"""
    resource_identifier: NotRequired["str"]
    """<p>The unique identifier of the AWS resource within its service.</p>"""
    resource_arn: NotRequired["aws_sdk_partnercentral_benefits.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the AWS resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociatedResource) -> dict:
    out: dict = {}
    if "resource_type" in value:
        import aws_sdk_partnercentral_benefits.types.resource_type

        out["ResourceType"] = (
            aws_sdk_partnercentral_benefits.types.resource_type.serialize_aws_json_1_0(
                value["resource_type"]
            )
        )
    if "resource_identifier" in value:
        out["ResourceIdentifier"] = value["resource_identifier"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociatedResource:
    out: AssociatedResource = {}  # type: ignore[typeddict-item]
    if "ResourceType" in data:
        import aws_sdk_partnercentral_benefits.types.resource_type

        out["resource_type"] = (
            aws_sdk_partnercentral_benefits.types.resource_type.deserialize_aws_json_1_0(
                data["ResourceType"]
            )
        )
    if "ResourceIdentifier" in data:
        out["resource_identifier"] = data["ResourceIdentifier"]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    return out
