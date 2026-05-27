"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVerifiedAccessEndpointRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.certificate_arn
    import aws_sdk_ec2.types.create_verified_access_endpoint_cidr_options
    import aws_sdk_ec2.types.create_verified_access_endpoint_eni_options
    import aws_sdk_ec2.types.create_verified_access_endpoint_load_balancer_options
    import aws_sdk_ec2.types.create_verified_access_endpoint_rds_options
    import aws_sdk_ec2.types.security_group_id_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list
    import aws_sdk_ec2.types.verified_access_endpoint_attachment_type
    import aws_sdk_ec2.types.verified_access_endpoint_type
    import aws_sdk_ec2.types.verified_access_group_id
    import aws_sdk_ec2.types.verified_access_sse_specification_request


class CreateVerifiedAccessEndpointRequest(TypedDict):
    verified_access_group_id: NotRequired[
        "aws_sdk_ec2.types.verified_access_group_id.VerifiedAccessGroupId"
    ]
    """<p>The ID of the Verified Access group to associate the endpoint with.</p>"""
    endpoint_type: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_type.VerifiedAccessEndpointType"
    ]
    """<p>The type of Verified Access endpoint to create.</p>"""
    attachment_type: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_attachment_type.VerifiedAccessEndpointAttachmentType"
    ]
    """<p>The type of attachment.</p>"""
    domain_certificate_arn: NotRequired[
        "aws_sdk_ec2.types.certificate_arn.CertificateArn"
    ]
    """<p>The ARN of the public TLS/SSL certificate in Amazon Web Services Certificate Manager to associate with the endpoint. The CN in the certificate must match the DNS name your end users will use to reach your application.</p>"""
    application_domain: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The DNS name for users to reach your application.</p>"""
    endpoint_domain_prefix: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A custom identifier that is prepended to the DNS name that is generated for the endpoint.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_ec2.types.security_group_id_list.SecurityGroupIdList"
    ]
    """<p>The IDs of the security groups to associate with the Verified Access endpoint. Required if <code>AttachmentType</code> is set to <code>vpc</code>.</p>"""
    load_balancer_options: NotRequired[
        "aws_sdk_ec2.types.create_verified_access_endpoint_load_balancer_options.CreateVerifiedAccessEndpointLoadBalancerOptions"
    ]
    """<p>The load balancer details. This parameter is required if the endpoint type is <code>load-balancer</code>.</p>"""
    network_interface_options: NotRequired[
        "aws_sdk_ec2.types.create_verified_access_endpoint_eni_options.CreateVerifiedAccessEndpointEniOptions"
    ]
    """<p>The network interface details. This parameter is required if the endpoint type is <code>network-interface</code>.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description for the Verified Access endpoint.</p>"""
    policy_document: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Verified Access policy document.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to assign to the Verified Access endpoint.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency</a>.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    sse_specification: NotRequired[
        "aws_sdk_ec2.types.verified_access_sse_specification_request.VerifiedAccessSseSpecificationRequest"
    ]
    """<p>The options for server side encryption.</p>"""
    rds_options: NotRequired[
        "aws_sdk_ec2.types.create_verified_access_endpoint_rds_options.CreateVerifiedAccessEndpointRdsOptions"
    ]
    """<p>The RDS details. This parameter is required if the endpoint type is <code>rds</code>.</p>"""
    cidr_options: NotRequired[
        "aws_sdk_ec2.types.create_verified_access_endpoint_cidr_options.CreateVerifiedAccessEndpointCidrOptions"
    ]
    """<p>The CIDR options. This parameter is required if the endpoint type is <code>cidr</code>.</p>"""
