"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessEndpoint``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

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


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VerifiedAccessEndpoint, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "verified_access_instance_id" in value:
        pairs.append(
            (
                f"{prefix}.VerifiedAccessInstanceId",
                str(value["verified_access_instance_id"]),
            )
        )
    if "verified_access_group_id" in value:
        pairs.append(
            (f"{prefix}.VerifiedAccessGroupId", str(value["verified_access_group_id"]))
        )
    if "verified_access_endpoint_id" in value:
        pairs.append(
            (
                f"{prefix}.VerifiedAccessEndpointId",
                str(value["verified_access_endpoint_id"]),
            )
        )
    if "application_domain" in value:
        pairs.append((f"{prefix}.ApplicationDomain", str(value["application_domain"])))
    if "endpoint_type" in value:
        import aws_sdk_ec2.types.verified_access_endpoint_type

        aws_sdk_ec2.types.verified_access_endpoint_type.serialize_ec2_query(
            value["endpoint_type"], pairs, f"{prefix}.EndpointType"
        )
    if "attachment_type" in value:
        import aws_sdk_ec2.types.verified_access_endpoint_attachment_type

        aws_sdk_ec2.types.verified_access_endpoint_attachment_type.serialize_ec2_query(
            value["attachment_type"], pairs, f"{prefix}.AttachmentType"
        )
    if "domain_certificate_arn" in value:
        pairs.append(
            (f"{prefix}.DomainCertificateArn", str(value["domain_certificate_arn"]))
        )
    if "endpoint_domain" in value:
        pairs.append((f"{prefix}.EndpointDomain", str(value["endpoint_domain"])))
    if "device_validation_domain" in value:
        pairs.append(
            (f"{prefix}.DeviceValidationDomain", str(value["device_validation_domain"]))
        )
    if "security_group_ids" in value:
        import aws_sdk_ec2.types.security_group_id_list

        aws_sdk_ec2.types.security_group_id_list.serialize_ec2_query(
            value["security_group_ids"], pairs, f"{prefix}.SecurityGroupIdSet"
        )
    if "load_balancer_options" in value:
        import aws_sdk_ec2.types.verified_access_endpoint_load_balancer_options

        aws_sdk_ec2.types.verified_access_endpoint_load_balancer_options.serialize_ec2_query(
            value["load_balancer_options"], pairs, f"{prefix}.LoadBalancerOptions"
        )
    if "network_interface_options" in value:
        import aws_sdk_ec2.types.verified_access_endpoint_eni_options

        aws_sdk_ec2.types.verified_access_endpoint_eni_options.serialize_ec2_query(
            value["network_interface_options"],
            pairs,
            f"{prefix}.NetworkInterfaceOptions",
        )
    if "status" in value:
        import aws_sdk_ec2.types.verified_access_endpoint_status

        aws_sdk_ec2.types.verified_access_endpoint_status.serialize_ec2_query(
            value["status"], pairs, f"{prefix}.Status"
        )
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "creation_time" in value:
        pairs.append((f"{prefix}.CreationTime", str(value["creation_time"])))
    if "last_updated_time" in value:
        pairs.append((f"{prefix}.LastUpdatedTime", str(value["last_updated_time"])))
    if "deletion_time" in value:
        pairs.append((f"{prefix}.DeletionTime", str(value["deletion_time"])))
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )
    if "sse_specification" in value:
        import aws_sdk_ec2.types.verified_access_sse_specification_response

        aws_sdk_ec2.types.verified_access_sse_specification_response.serialize_ec2_query(
            value["sse_specification"], pairs, f"{prefix}.SseSpecification"
        )
    if "rds_options" in value:
        import aws_sdk_ec2.types.verified_access_endpoint_rds_options

        aws_sdk_ec2.types.verified_access_endpoint_rds_options.serialize_ec2_query(
            value["rds_options"], pairs, f"{prefix}.RdsOptions"
        )
    if "cidr_options" in value:
        import aws_sdk_ec2.types.verified_access_endpoint_cidr_options

        aws_sdk_ec2.types.verified_access_endpoint_cidr_options.serialize_ec2_query(
            value["cidr_options"], pairs, f"{prefix}.CidrOptions"
        )


def deserialize_ec2_query(el: Element) -> VerifiedAccessEndpoint:
    out: VerifiedAccessEndpoint = {}  # type: ignore[typeddict-item]
    child_verified_access_instance_id = el.find("VerifiedAccessInstanceId")
    if child_verified_access_instance_id is not None:
        out["verified_access_instance_id"] = str(
            child_verified_access_instance_id.text or ""
        )
    child_verified_access_group_id = el.find("VerifiedAccessGroupId")
    if child_verified_access_group_id is not None:
        out["verified_access_group_id"] = str(child_verified_access_group_id.text or "")
    child_verified_access_endpoint_id = el.find("VerifiedAccessEndpointId")
    if child_verified_access_endpoint_id is not None:
        out["verified_access_endpoint_id"] = str(
            child_verified_access_endpoint_id.text or ""
        )
    child_application_domain = el.find("ApplicationDomain")
    if child_application_domain is not None:
        out["application_domain"] = str(child_application_domain.text or "")
    child_endpoint_type = el.find("EndpointType")
    if child_endpoint_type is not None:
        import aws_sdk_ec2.types.verified_access_endpoint_type

        out["endpoint_type"] = (
            aws_sdk_ec2.types.verified_access_endpoint_type.deserialize_ec2_query(
                child_endpoint_type
            )
        )
    child_attachment_type = el.find("AttachmentType")
    if child_attachment_type is not None:
        import aws_sdk_ec2.types.verified_access_endpoint_attachment_type

        out["attachment_type"] = (
            aws_sdk_ec2.types.verified_access_endpoint_attachment_type.deserialize_ec2_query(
                child_attachment_type
            )
        )
    child_domain_certificate_arn = el.find("DomainCertificateArn")
    if child_domain_certificate_arn is not None:
        out["domain_certificate_arn"] = str(child_domain_certificate_arn.text or "")
    child_endpoint_domain = el.find("EndpointDomain")
    if child_endpoint_domain is not None:
        out["endpoint_domain"] = str(child_endpoint_domain.text or "")
    child_device_validation_domain = el.find("DeviceValidationDomain")
    if child_device_validation_domain is not None:
        out["device_validation_domain"] = str(child_device_validation_domain.text or "")
    if el.find("SecurityGroupIdSet") is not None:
        import aws_sdk_ec2.types.security_group_id_list

        out["security_group_ids"] = (
            aws_sdk_ec2.types.security_group_id_list.deserialize_ec2_query(
                el, "SecurityGroupIdSet"
            )
        )
    child_load_balancer_options = el.find("LoadBalancerOptions")
    if child_load_balancer_options is not None:
        import aws_sdk_ec2.types.verified_access_endpoint_load_balancer_options

        out["load_balancer_options"] = (
            aws_sdk_ec2.types.verified_access_endpoint_load_balancer_options.deserialize_ec2_query(
                child_load_balancer_options
            )
        )
    child_network_interface_options = el.find("NetworkInterfaceOptions")
    if child_network_interface_options is not None:
        import aws_sdk_ec2.types.verified_access_endpoint_eni_options

        out["network_interface_options"] = (
            aws_sdk_ec2.types.verified_access_endpoint_eni_options.deserialize_ec2_query(
                child_network_interface_options
            )
        )
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_ec2.types.verified_access_endpoint_status

        out["status"] = (
            aws_sdk_ec2.types.verified_access_endpoint_status.deserialize_ec2_query(
                child_status
            )
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_creation_time = el.find("CreationTime")
    if child_creation_time is not None:
        out["creation_time"] = str(child_creation_time.text or "")
    child_last_updated_time = el.find("LastUpdatedTime")
    if child_last_updated_time is not None:
        out["last_updated_time"] = str(child_last_updated_time.text or "")
    child_deletion_time = el.find("DeletionTime")
    if child_deletion_time is not None:
        out["deletion_time"] = str(child_deletion_time.text or "")
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_sse_specification = el.find("SseSpecification")
    if child_sse_specification is not None:
        import aws_sdk_ec2.types.verified_access_sse_specification_response

        out["sse_specification"] = (
            aws_sdk_ec2.types.verified_access_sse_specification_response.deserialize_ec2_query(
                child_sse_specification
            )
        )
    child_rds_options = el.find("RdsOptions")
    if child_rds_options is not None:
        import aws_sdk_ec2.types.verified_access_endpoint_rds_options

        out["rds_options"] = (
            aws_sdk_ec2.types.verified_access_endpoint_rds_options.deserialize_ec2_query(
                child_rds_options
            )
        )
    child_cidr_options = el.find("CidrOptions")
    if child_cidr_options is not None:
        import aws_sdk_ec2.types.verified_access_endpoint_cidr_options

        out["cidr_options"] = (
            aws_sdk_ec2.types.verified_access_endpoint_cidr_options.deserialize_ec2_query(
                child_cidr_options
            )
        )
    return out
