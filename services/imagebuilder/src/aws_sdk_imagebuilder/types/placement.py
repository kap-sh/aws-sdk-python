"""Generated from Smithy shape ``com.amazonaws.imagebuilder#Placement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.tenancy_type


class Placement(TypedDict, closed=True):
    availability_zone: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Availability Zone where your build and test instances will launch.</p>"""
    tenancy: NotRequired["aws_sdk_imagebuilder.types.tenancy_type.TenancyType"]
    """<p>The tenancy of the instance. An instance with a tenancy of <code>dedicated</code> runs on single-tenant hardware. An instance with a tenancy of <code>host</code> runs on a Dedicated Host.</p> <p>If tenancy is set to <code>host</code>, then you can optionally specify one target for placement – either host ID or host resource group ARN. If automatic placement is enabled for your host, and you don't specify any placement target, Amazon EC2 will try to find an available host for your build and test instances.</p>"""
    host_id: NotRequired["aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the Dedicated Host on which build and test instances run. This only applies if <code>tenancy</code> is <code>host</code>. If you specify the host ID, you must not specify the resource group ARN. If you specify both, Image Builder returns an error.</p>"""
    host_resource_group_arn: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon Resource Name (ARN) of the host resource group in which to launch build and test instances. This only applies if <code>tenancy</code> is <code>host</code>. If you specify the resource group ARN, you must not specify the host ID. If you specify both, Image Builder returns an error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Placement) -> dict:
    out: dict = {}
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "tenancy" in value:
        import aws_sdk_imagebuilder.types.tenancy_type

        out["tenancy"] = aws_sdk_imagebuilder.types.tenancy_type.serialize_json(
            value["tenancy"]
        )
    if "host_id" in value:
        out["hostId"] = value["host_id"]
    if "host_resource_group_arn" in value:
        out["hostResourceGroupArn"] = value["host_resource_group_arn"]
    return out


def deserialize_json(data: dict) -> Placement:
    out: Placement = {}  # type: ignore[typeddict-item]
    if "availabilityZone" in data:
        out["availability_zone"] = data["availabilityZone"]
    if "tenancy" in data:
        import aws_sdk_imagebuilder.types.tenancy_type

        out["tenancy"] = aws_sdk_imagebuilder.types.tenancy_type.deserialize_json(
            data["tenancy"]
        )
    if "hostId" in data:
        out["host_id"] = data["hostId"]
    if "hostResourceGroupArn" in data:
        out["host_resource_group_arn"] = data["hostResourceGroupArn"]
    return out
