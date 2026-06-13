"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#ConnectorSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_pca_connector_scep.types.certificate_authority_arn
    import aws_sdk_pca_connector_scep.types.connector_arn
    import aws_sdk_pca_connector_scep.types.connector_status
    import aws_sdk_pca_connector_scep.types.connector_status_reason
    import aws_sdk_pca_connector_scep.types.connector_type
    import aws_sdk_pca_connector_scep.types.mobile_device_management
    import aws_sdk_pca_connector_scep.types.open_id_configuration


class ConnectorSummary(TypedDict):
    arn: NotRequired["aws_sdk_pca_connector_scep.types.connector_arn.ConnectorArn"]
    """<p>The Amazon Resource Name (ARN) of the connector.</p>"""
    certificate_authority_arn: NotRequired[
        "aws_sdk_pca_connector_scep.types.certificate_authority_arn.CertificateAuthorityArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the connector's associated certificate authority.</p>"""
    type: NotRequired["aws_sdk_pca_connector_scep.types.connector_type.ConnectorType"]
    """<p>The connector type.</p>"""
    mobile_device_management: NotRequired[
        "aws_sdk_pca_connector_scep.types.mobile_device_management.MobileDeviceManagement"
    ]
    """<p>Contains settings relevant to the mobile device management system that you chose for the connector. If you didn't configure <code>MobileDeviceManagement</code>, then the connector is for general-purpose use and this object is empty.</p>"""
    open_id_configuration: NotRequired[
        "aws_sdk_pca_connector_scep.types.open_id_configuration.OpenIdConfiguration"
    ]
    """<p>Contains OpenID Connect (OIDC) parameters for use with Microsoft Intune.</p>"""
    status: NotRequired[
        "aws_sdk_pca_connector_scep.types.connector_status.ConnectorStatus"
    ]
    """<p>The connector's status. Status can be creating, active, deleting, or failed.</p>"""
    status_reason: NotRequired[
        "aws_sdk_pca_connector_scep.types.connector_status_reason.ConnectorStatusReason"
    ]
    """<p>Information about why connector creation failed, if status is <code>FAILED</code>.</p>"""
    endpoint: NotRequired["str"]
    """<p>The connector's HTTPS public SCEP URL.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the challenge was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the challenge was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "certificate_authority_arn" in value:
        out["CertificateAuthorityArn"] = value["certificate_authority_arn"]
    if "type" in value:
        import aws_sdk_pca_connector_scep.types.connector_type

        out["Type"] = aws_sdk_pca_connector_scep.types.connector_type.serialize_json(
            value["type"]
        )
    if "mobile_device_management" in value:
        import aws_sdk_pca_connector_scep.types.mobile_device_management

        out["MobileDeviceManagement"] = (
            aws_sdk_pca_connector_scep.types.mobile_device_management.serialize_json(
                value["mobile_device_management"]
            )
        )
    if "open_id_configuration" in value:
        import aws_sdk_pca_connector_scep.types.open_id_configuration

        out["OpenIdConfiguration"] = (
            aws_sdk_pca_connector_scep.types.open_id_configuration.serialize_json(
                value["open_id_configuration"]
            )
        )
    if "status" in value:
        import aws_sdk_pca_connector_scep.types.connector_status

        out["Status"] = (
            aws_sdk_pca_connector_scep.types.connector_status.serialize_json(
                value["status"]
            )
        )
    if "status_reason" in value:
        import aws_sdk_pca_connector_scep.types.connector_status_reason

        out["StatusReason"] = (
            aws_sdk_pca_connector_scep.types.connector_status_reason.serialize_json(
                value["status_reason"]
            )
        )
    if "endpoint" in value:
        out["Endpoint"] = value["endpoint"]
    if "created_at" in value:
        import aws_sdk_pca_connector_scep.types._prelude.timestamp

        out["CreatedAt"] = (
            aws_sdk_pca_connector_scep.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_pca_connector_scep.types._prelude.timestamp

        out["UpdatedAt"] = (
            aws_sdk_pca_connector_scep.types._prelude.timestamp.serialize_json(
                value["updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConnectorSummary:
    out: ConnectorSummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "CertificateAuthorityArn" in data:
        out["certificate_authority_arn"] = data["CertificateAuthorityArn"]
    if "Type" in data:
        import aws_sdk_pca_connector_scep.types.connector_type

        out["type"] = aws_sdk_pca_connector_scep.types.connector_type.deserialize_json(
            data["Type"]
        )
    if "MobileDeviceManagement" in data:
        import aws_sdk_pca_connector_scep.types.mobile_device_management

        out["mobile_device_management"] = (
            aws_sdk_pca_connector_scep.types.mobile_device_management.deserialize_json(
                data["MobileDeviceManagement"]
            )
        )
    if "OpenIdConfiguration" in data:
        import aws_sdk_pca_connector_scep.types.open_id_configuration

        out["open_id_configuration"] = (
            aws_sdk_pca_connector_scep.types.open_id_configuration.deserialize_json(
                data["OpenIdConfiguration"]
            )
        )
    if "Status" in data:
        import aws_sdk_pca_connector_scep.types.connector_status

        out["status"] = (
            aws_sdk_pca_connector_scep.types.connector_status.deserialize_json(
                data["Status"]
            )
        )
    if "StatusReason" in data:
        import aws_sdk_pca_connector_scep.types.connector_status_reason

        out["status_reason"] = (
            aws_sdk_pca_connector_scep.types.connector_status_reason.deserialize_json(
                data["StatusReason"]
            )
        )
    if "Endpoint" in data:
        out["endpoint"] = data["Endpoint"]
    if "CreatedAt" in data:
        import aws_sdk_pca_connector_scep.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_pca_connector_scep.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    if "UpdatedAt" in data:
        import aws_sdk_pca_connector_scep.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_pca_connector_scep.types._prelude.timestamp.deserialize_json(
                data["UpdatedAt"]
            )
        )
    return out
