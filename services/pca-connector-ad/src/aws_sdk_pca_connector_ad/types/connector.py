"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#Connector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_pca_connector_ad.types.certificate_authority_arn
    import aws_sdk_pca_connector_ad.types.connector_arn
    import aws_sdk_pca_connector_ad.types.connector_status
    import aws_sdk_pca_connector_ad.types.connector_status_reason
    import aws_sdk_pca_connector_ad.types.directory_id
    import aws_sdk_pca_connector_ad.types.vpc_information


class Connector(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_pca_connector_ad.types.connector_arn.ConnectorArn"]
    r"""<p>The Amazon Resource Name (ARN) that was returned when you called <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html\">CreateConnector</a>. </p>"""
    certificate_authority_arn: NotRequired[
        "aws_sdk_pca_connector_ad.types.certificate_authority_arn.CertificateAuthorityArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the certificate authority being used. </p>"""
    certificate_enrollment_policy_server_endpoint: NotRequired["str"]
    """<p>Certificate enrollment endpoint for Active Directory domain-joined objects reach out to when requesting certificates.</p>"""
    directory_id: NotRequired["aws_sdk_pca_connector_ad.types.directory_id.DirectoryId"]
    """<p>The identifier of the Active Directory.</p>"""
    vpc_information: NotRequired[
        "aws_sdk_pca_connector_ad.types.vpc_information.VpcInformation"
    ]
    """<p>Information of the VPC and security group(s) used with the connector.</p>"""
    status: NotRequired[
        "aws_sdk_pca_connector_ad.types.connector_status.ConnectorStatus"
    ]
    """<p>Status of the connector. Status can be creating, active, deleting, or failed.</p>"""
    status_reason: NotRequired[
        "aws_sdk_pca_connector_ad.types.connector_status_reason.ConnectorStatusReason"
    ]
    """<p>Additional information about the connector status if the status is failed.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the connector was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the connector was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Connector) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "certificate_authority_arn" in value:
        out["CertificateAuthorityArn"] = value["certificate_authority_arn"]
    if "certificate_enrollment_policy_server_endpoint" in value:
        out["CertificateEnrollmentPolicyServerEndpoint"] = value[
            "certificate_enrollment_policy_server_endpoint"
        ]
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "vpc_information" in value:
        import aws_sdk_pca_connector_ad.types.vpc_information

        out["VpcInformation"] = (
            aws_sdk_pca_connector_ad.types.vpc_information.serialize_json(
                value["vpc_information"]
            )
        )
    if "status" in value:
        import aws_sdk_pca_connector_ad.types.connector_status

        out["Status"] = aws_sdk_pca_connector_ad.types.connector_status.serialize_json(
            value["status"]
        )
    if "status_reason" in value:
        import aws_sdk_pca_connector_ad.types.connector_status_reason

        out["StatusReason"] = (
            aws_sdk_pca_connector_ad.types.connector_status_reason.serialize_json(
                value["status_reason"]
            )
        )
    if "created_at" in value:
        import aws_sdk_pca_connector_ad.types._prelude.timestamp

        out["CreatedAt"] = (
            aws_sdk_pca_connector_ad.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_pca_connector_ad.types._prelude.timestamp

        out["UpdatedAt"] = (
            aws_sdk_pca_connector_ad.types._prelude.timestamp.serialize_json(
                value["updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> Connector:
    out: Connector = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "CertificateAuthorityArn" in data:
        out["certificate_authority_arn"] = data["CertificateAuthorityArn"]
    if "CertificateEnrollmentPolicyServerEndpoint" in data:
        out["certificate_enrollment_policy_server_endpoint"] = data[
            "CertificateEnrollmentPolicyServerEndpoint"
        ]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    if "VpcInformation" in data:
        import aws_sdk_pca_connector_ad.types.vpc_information

        out["vpc_information"] = (
            aws_sdk_pca_connector_ad.types.vpc_information.deserialize_json(
                data["VpcInformation"]
            )
        )
    if "Status" in data:
        import aws_sdk_pca_connector_ad.types.connector_status

        out["status"] = (
            aws_sdk_pca_connector_ad.types.connector_status.deserialize_json(
                data["Status"]
            )
        )
    if "StatusReason" in data:
        import aws_sdk_pca_connector_ad.types.connector_status_reason

        out["status_reason"] = (
            aws_sdk_pca_connector_ad.types.connector_status_reason.deserialize_json(
                data["StatusReason"]
            )
        )
    if "CreatedAt" in data:
        import aws_sdk_pca_connector_ad.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_pca_connector_ad.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    if "UpdatedAt" in data:
        import aws_sdk_pca_connector_ad.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_pca_connector_ad.types._prelude.timestamp.deserialize_json(
                data["UpdatedAt"]
            )
        )
    return out
