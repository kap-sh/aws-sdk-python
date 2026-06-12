"""Generated from Smithy shape ``com.amazonaws.fsx#S3AccessPoint``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.general_arn
    import aws_sdk_fsx.types.s3_access_point_alias
    import aws_sdk_fsx.types.s3_access_point_vpc_configuration


class S3AccessPoint(TypedDict):
    resource_arn: NotRequired["aws_sdk_fsx.types.general_arn.GeneralARN"]
    """<p>he S3 access point's ARN.</p>"""
    alias: NotRequired["aws_sdk_fsx.types.s3_access_point_alias.S3AccessPointAlias"]
    """<p>The S3 access point's alias.</p>"""
    vpc_configuration: NotRequired[
        "aws_sdk_fsx.types.s3_access_point_vpc_configuration.S3AccessPointVpcConfiguration"
    ]
    """<p>The S3 access point's virtual private cloud (VPC) configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3AccessPoint) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    if "alias" in value:
        out["Alias"] = value["alias"]
    if "vpc_configuration" in value:
        import aws_sdk_fsx.types.s3_access_point_vpc_configuration

        out["VpcConfiguration"] = (
            aws_sdk_fsx.types.s3_access_point_vpc_configuration.serialize_aws_json_1_1(
                value["vpc_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> S3AccessPoint:
    out: S3AccessPoint = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    if "Alias" in data:
        out["alias"] = data["Alias"]
    if "VpcConfiguration" in data:
        import aws_sdk_fsx.types.s3_access_point_vpc_configuration

        out["vpc_configuration"] = (
            aws_sdk_fsx.types.s3_access_point_vpc_configuration.deserialize_aws_json_1_1(
                data["VpcConfiguration"]
            )
        )
    return out
