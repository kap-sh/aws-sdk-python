"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessEndpoint``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.security_group_id_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.verified_access_endpoint_attachment_type
    import aws_sdk_ec2.types.verified_access_endpoint_cidr_options
    import aws_sdk_ec2.types.verified_access_endpoint_eni_options
    import aws_sdk_ec2.types.verified_access_endpoint_load_balancer_options
    import aws_sdk_ec2.types.verified_access_endpoint_rds_options
    import aws_sdk_ec2.types.verified_access_endpoint_status
    import aws_sdk_ec2.types.verified_access_endpoint_type
    import aws_sdk_ec2.types.verified_access_sse_specification_response


class VerifiedAccessEndpoint(TypedDict):
    verified_access_instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services Verified Access instance.</p>"""
    verified_access_group_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services Verified Access group.</p>"""
    verified_access_endpoint_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services Verified Access endpoint.</p>"""
    application_domain: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The DNS name for users to reach your application.</p>"""
    endpoint_type: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_type.VerifiedAccessEndpointType"
    ]
    """<p>The type of Amazon Web Services Verified Access endpoint. Incoming application requests will be sent to an IP address, load balancer or a network interface depending on the endpoint type specified.</p>"""
    attachment_type: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_attachment_type.VerifiedAccessEndpointAttachmentType"
    ]
    """<p>The type of attachment used to provide connectivity between the Amazon Web Services Verified Access endpoint and the application.</p>"""
    domain_certificate_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of a public TLS/SSL certificate imported into or created with ACM.</p>"""
    endpoint_domain: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A DNS name that is generated for the endpoint.</p>"""
    device_validation_domain: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Returned if endpoint has a device trust provider attached.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_ec2.types.security_group_id_list.SecurityGroupIdList"
    ]
    """<p>The IDs of the security groups for the endpoint.</p>"""
    load_balancer_options: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_load_balancer_options.VerifiedAccessEndpointLoadBalancerOptions"
    ]
    """<p>The load balancer details if creating the Amazon Web Services Verified Access endpoint as <code>load-balancer</code>type.</p>"""
    network_interface_options: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_eni_options.VerifiedAccessEndpointEniOptions"
    ]
    """<p>The options for network-interface type endpoint.</p>"""
    status: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_status.VerifiedAccessEndpointStatus"
    ]
    """<p>The endpoint status.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description for the Amazon Web Services Verified Access endpoint.</p>"""
    creation_time: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The creation time.</p>"""
    last_updated_time: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The last updated time.</p>"""
    deletion_time: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The deletion time.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags.</p>"""
    sse_specification: NotRequired[
        "aws_sdk_ec2.types.verified_access_sse_specification_response.VerifiedAccessSseSpecificationResponse"
    ]
    """<p>The options in use for server side encryption.</p>"""
    rds_options: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_rds_options.VerifiedAccessEndpointRdsOptions"
    ]
    """<p>The options for an RDS endpoint.</p>"""
    cidr_options: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_cidr_options.VerifiedAccessEndpointCidrOptions"
    ]
    """<p>The options for a CIDR endpoint.</p>"""
