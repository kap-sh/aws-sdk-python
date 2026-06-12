"""Generated from Smithy shape ``com.amazonaws.osis#VpcOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_osis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_osis.types.security_group_ids
    import aws_sdk_osis.types.subnet_ids
    import aws_sdk_osis.types.vpc_attachment_options
    import aws_sdk_osis.types.vpc_endpoint_management


class VpcOptions(TypedDict):
    subnet_ids: "aws_sdk_osis.types.subnet_ids.SubnetIds"
    """<p>A list of subnet IDs associated with the VPC endpoint.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_osis.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>A list of security groups associated with the VPC endpoint.</p>"""
    vpc_attachment_options: NotRequired[
        "aws_sdk_osis.types.vpc_attachment_options.VpcAttachmentOptions"
    ]
    """<p>Options for attaching a VPC to a pipeline.</p>"""
    vpc_endpoint_management: NotRequired[
        "aws_sdk_osis.types.vpc_endpoint_management.VpcEndpointManagement"
    ]
    """<p>Defines whether you or Amazon OpenSearch Ingestion service create and manage the VPC endpoint configured for the pipeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcOptions) -> dict:
    out: dict = {}
    import aws_sdk_osis.types.subnet_ids

    out["SubnetIds"] = aws_sdk_osis.types.subnet_ids.serialize_json(value["subnet_ids"])
    if "security_group_ids" in value:
        import aws_sdk_osis.types.security_group_ids

        out["SecurityGroupIds"] = aws_sdk_osis.types.security_group_ids.serialize_json(
            value["security_group_ids"]
        )
    if "vpc_attachment_options" in value:
        import aws_sdk_osis.types.vpc_attachment_options

        out["VpcAttachmentOptions"] = (
            aws_sdk_osis.types.vpc_attachment_options.serialize_json(
                value["vpc_attachment_options"]
            )
        )
    if "vpc_endpoint_management" in value:
        import aws_sdk_osis.types.vpc_endpoint_management

        out["VpcEndpointManagement"] = (
            aws_sdk_osis.types.vpc_endpoint_management.serialize_json(
                value["vpc_endpoint_management"]
            )
        )
    return out


def deserialize_json(data: dict) -> VpcOptions:
    out: VpcOptions = {}  # type: ignore[typeddict-item]
    if "SubnetIds" in data:
        import aws_sdk_osis.types.subnet_ids

        out["subnet_ids"] = aws_sdk_osis.types.subnet_ids.deserialize_json(
            data["SubnetIds"]
        )
    else:
        raise DeserializationError("VpcOptions.subnet_ids required")
    if "SecurityGroupIds" in data:
        import aws_sdk_osis.types.security_group_ids

        out["security_group_ids"] = (
            aws_sdk_osis.types.security_group_ids.deserialize_json(
                data["SecurityGroupIds"]
            )
        )
    if "VpcAttachmentOptions" in data:
        import aws_sdk_osis.types.vpc_attachment_options

        out["vpc_attachment_options"] = (
            aws_sdk_osis.types.vpc_attachment_options.deserialize_json(
                data["VpcAttachmentOptions"]
            )
        )
    if "VpcEndpointManagement" in data:
        import aws_sdk_osis.types.vpc_endpoint_management

        out["vpc_endpoint_management"] = (
            aws_sdk_osis.types.vpc_endpoint_management.deserialize_json(
                data["VpcEndpointManagement"]
            )
        )
    return out
