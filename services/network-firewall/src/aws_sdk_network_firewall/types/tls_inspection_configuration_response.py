"""Generated from Smithy shape ``com.amazonaws.networkfirewall#TLSInspectionConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.certificates
    import aws_sdk_network_firewall.types.description
    import aws_sdk_network_firewall.types.encryption_configuration
    import aws_sdk_network_firewall.types.last_update_time
    import aws_sdk_network_firewall.types.number_of_associations
    import aws_sdk_network_firewall.types.resource_arn
    import aws_sdk_network_firewall.types.resource_id
    import aws_sdk_network_firewall.types.resource_name
    import aws_sdk_network_firewall.types.resource_status
    import aws_sdk_network_firewall.types.tag_list
    import aws_sdk_network_firewall.types.tls_certificate_data


class TLSInspectionConfigurationResponse(TypedDict):
    tls_inspection_configuration_arn: (
        "aws_sdk_network_firewall.types.resource_arn.ResourceArn"
    )
    """<p>The Amazon Resource Name (ARN) of the TLS inspection configuration.</p>"""
    tls_inspection_configuration_name: (
        "aws_sdk_network_firewall.types.resource_name.ResourceName"
    )
    """<p>The descriptive name of the TLS inspection configuration. You can't change the name of a TLS inspection configuration after you create it.</p>"""
    tls_inspection_configuration_id: (
        "aws_sdk_network_firewall.types.resource_id.ResourceId"
    )
    """<p>A unique identifier for the TLS inspection configuration. This ID is returned in the responses to create and list commands. You provide it to operations such as update and delete.</p>"""
    tls_inspection_configuration_status: NotRequired[
        "aws_sdk_network_firewall.types.resource_status.ResourceStatus"
    ]
    """<p>Detailed information about the current status of a <a>TLSInspectionConfiguration</a>. You can retrieve this for a TLS inspection configuration by calling <a>DescribeTLSInspectionConfiguration</a> and providing the TLS inspection configuration name and ARN.</p>"""
    description: NotRequired["aws_sdk_network_firewall.types.description.Description"]
    """<p>A description of the TLS inspection configuration. </p>"""
    tags: NotRequired["aws_sdk_network_firewall.types.tag_list.TagList"]
    """<p>The key:value pairs to associate with the resource.</p>"""
    last_modified_time: NotRequired[
        "aws_sdk_network_firewall.types.last_update_time.LastUpdateTime"
    ]
    """<p>The last time that the TLS inspection configuration was changed.</p>"""
    number_of_associations: NotRequired[
        "aws_sdk_network_firewall.types.number_of_associations.NumberOfAssociations"
    ]
    """<p>The number of firewall policies that use this TLS inspection configuration.</p>"""
    encryption_configuration: NotRequired[
        "aws_sdk_network_firewall.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>A complex type that contains the Amazon Web Services KMS encryption configuration settings for your TLS inspection configuration.</p>"""
    certificates: NotRequired[
        "aws_sdk_network_firewall.types.certificates.Certificates"
    ]
    """<p>A list of the certificates associated with the TLS inspection configuration.</p>"""
    certificate_authority: NotRequired[
        "aws_sdk_network_firewall.types.tls_certificate_data.TlsCertificateData"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TLSInspectionConfigurationResponse) -> dict:
    out: dict = {}
    out["TLSInspectionConfigurationArn"] = value["tls_inspection_configuration_arn"]
    out["TLSInspectionConfigurationName"] = value["tls_inspection_configuration_name"]
    out["TLSInspectionConfigurationId"] = value["tls_inspection_configuration_id"]
    if "tls_inspection_configuration_status" in value:
        import aws_sdk_network_firewall.types.resource_status

        out["TLSInspectionConfigurationStatus"] = (
            aws_sdk_network_firewall.types.resource_status.serialize_aws_json_1_0(
                value["tls_inspection_configuration_status"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import aws_sdk_network_firewall.types.tag_list

        out["Tags"] = aws_sdk_network_firewall.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "last_modified_time" in value:
        import aws_sdk_network_firewall.types.last_update_time

        out["LastModifiedTime"] = (
            aws_sdk_network_firewall.types.last_update_time.serialize_aws_json_1_0(
                value["last_modified_time"]
            )
        )
    if "number_of_associations" in value:
        out["NumberOfAssociations"] = value["number_of_associations"]
    if "encryption_configuration" in value:
        import aws_sdk_network_firewall.types.encryption_configuration

        out["EncryptionConfiguration"] = (
            aws_sdk_network_firewall.types.encryption_configuration.serialize_aws_json_1_0(
                value["encryption_configuration"]
            )
        )
    if "certificates" in value:
        import aws_sdk_network_firewall.types.certificates

        out["Certificates"] = (
            aws_sdk_network_firewall.types.certificates.serialize_aws_json_1_0(
                value["certificates"]
            )
        )
    if "certificate_authority" in value:
        import aws_sdk_network_firewall.types.tls_certificate_data

        out["CertificateAuthority"] = (
            aws_sdk_network_firewall.types.tls_certificate_data.serialize_aws_json_1_0(
                value["certificate_authority"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TLSInspectionConfigurationResponse:
    out: TLSInspectionConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "TLSInspectionConfigurationArn" in data:
        out["tls_inspection_configuration_arn"] = data["TLSInspectionConfigurationArn"]
    else:
        raise DeserializationError(
            "TLSInspectionConfigurationResponse.tls_inspection_configuration_arn required"
        )
    if "TLSInspectionConfigurationName" in data:
        out["tls_inspection_configuration_name"] = data[
            "TLSInspectionConfigurationName"
        ]
    else:
        raise DeserializationError(
            "TLSInspectionConfigurationResponse.tls_inspection_configuration_name required"
        )
    if "TLSInspectionConfigurationId" in data:
        out["tls_inspection_configuration_id"] = data["TLSInspectionConfigurationId"]
    else:
        raise DeserializationError(
            "TLSInspectionConfigurationResponse.tls_inspection_configuration_id required"
        )
    if "TLSInspectionConfigurationStatus" in data:
        import aws_sdk_network_firewall.types.resource_status

        out["tls_inspection_configuration_status"] = (
            aws_sdk_network_firewall.types.resource_status.deserialize_aws_json_1_0(
                data["TLSInspectionConfigurationStatus"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Tags" in data:
        import aws_sdk_network_firewall.types.tag_list

        out["tags"] = aws_sdk_network_firewall.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    if "LastModifiedTime" in data:
        import aws_sdk_network_firewall.types.last_update_time

        out["last_modified_time"] = (
            aws_sdk_network_firewall.types.last_update_time.deserialize_aws_json_1_0(
                data["LastModifiedTime"]
            )
        )
    if "NumberOfAssociations" in data:
        out["number_of_associations"] = data["NumberOfAssociations"]
    if "EncryptionConfiguration" in data:
        import aws_sdk_network_firewall.types.encryption_configuration

        out["encryption_configuration"] = (
            aws_sdk_network_firewall.types.encryption_configuration.deserialize_aws_json_1_0(
                data["EncryptionConfiguration"]
            )
        )
    if "Certificates" in data:
        import aws_sdk_network_firewall.types.certificates

        out["certificates"] = (
            aws_sdk_network_firewall.types.certificates.deserialize_aws_json_1_0(
                data["Certificates"]
            )
        )
    if "CertificateAuthority" in data:
        import aws_sdk_network_firewall.types.tls_certificate_data

        out["certificate_authority"] = (
            aws_sdk_network_firewall.types.tls_certificate_data.deserialize_aws_json_1_0(
                data["CertificateAuthority"]
            )
        )
    return out
