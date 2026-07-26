"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#ConnectorSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_pca_connector_scep.types.certificate_authority_arn
    import capo_pca_connector_scep.types.connector_arn
    import capo_pca_connector_scep.types.connector_status
    import capo_pca_connector_scep.types.connector_status_reason
    import capo_pca_connector_scep.types.connector_type
    import capo_pca_connector_scep.types.mobile_device_management
    import capo_pca_connector_scep.types.open_id_configuration


class ConnectorSummary(TypedDict, closed=True):
    arn: NotRequired["capo_pca_connector_scep.types.connector_arn.ConnectorArn"]
    """<p>The Amazon Resource Name (ARN) of the connector.</p>"""
    certificate_authority_arn: NotRequired[
        "capo_pca_connector_scep.types.certificate_authority_arn.CertificateAuthorityArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the connector's associated certificate authority.</p>"""
    type: NotRequired["capo_pca_connector_scep.types.connector_type.ConnectorType"]
    """<p>The connector type.</p>"""
    mobile_device_management: NotRequired[
        "capo_pca_connector_scep.types.mobile_device_management.MobileDeviceManagement"
    ]
    """<p>Contains settings relevant to the mobile device management system that you chose for the connector. If you didn't configure <code>MobileDeviceManagement</code>, then the connector is for general-purpose use and this object is empty.</p>"""
    open_id_configuration: NotRequired[
        "capo_pca_connector_scep.types.open_id_configuration.OpenIdConfiguration"
    ]
    """<p>Contains OpenID Connect (OIDC) parameters for use with Microsoft Intune.</p>"""
    status: NotRequired[
        "capo_pca_connector_scep.types.connector_status.ConnectorStatus"
    ]
    """<p>The connector's status. Status can be creating, active, deleting, or failed.</p>"""
    status_reason: NotRequired[
        "capo_pca_connector_scep.types.connector_status_reason.ConnectorStatusReason"
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
        import capo_pca_connector_scep.types.connector_type

        out["Type"] = capo_pca_connector_scep.types.connector_type.serialize_json(
            value["type"]
        )
    if "mobile_device_management" in value:
        import capo_pca_connector_scep.types.mobile_device_management

        out["MobileDeviceManagement"] = (
            capo_pca_connector_scep.types.mobile_device_management.serialize_json(
                value["mobile_device_management"]
            )
        )
    if "open_id_configuration" in value:
        import capo_pca_connector_scep.types.open_id_configuration

        out["OpenIdConfiguration"] = (
            capo_pca_connector_scep.types.open_id_configuration.serialize_json(
                value["open_id_configuration"]
            )
        )
    if "status" in value:
        import capo_pca_connector_scep.types.connector_status

        out["Status"] = capo_pca_connector_scep.types.connector_status.serialize_json(
            value["status"]
        )
    if "status_reason" in value:
        import capo_pca_connector_scep.types.connector_status_reason

        out["StatusReason"] = (
            capo_pca_connector_scep.types.connector_status_reason.serialize_json(
                value["status_reason"]
            )
        )
    if "endpoint" in value:
        out["Endpoint"] = value["endpoint"]
    if "created_at" in value:
        import capo_pca_connector_scep.types._prelude.timestamp

        out["CreatedAt"] = (
            capo_pca_connector_scep.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import capo_pca_connector_scep.types._prelude.timestamp

        out["UpdatedAt"] = (
            capo_pca_connector_scep.types._prelude.timestamp.serialize_json(
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
        import capo_pca_connector_scep.types.connector_type

        out["type"] = capo_pca_connector_scep.types.connector_type.deserialize_json(
            data["Type"]
        )
    if "MobileDeviceManagement" in data:
        import capo_pca_connector_scep.types.mobile_device_management

        out["mobile_device_management"] = (
            capo_pca_connector_scep.types.mobile_device_management.deserialize_json(
                data["MobileDeviceManagement"]
            )
        )
    if "OpenIdConfiguration" in data:
        import capo_pca_connector_scep.types.open_id_configuration

        out["open_id_configuration"] = (
            capo_pca_connector_scep.types.open_id_configuration.deserialize_json(
                data["OpenIdConfiguration"]
            )
        )
    if "Status" in data:
        import capo_pca_connector_scep.types.connector_status

        out["status"] = capo_pca_connector_scep.types.connector_status.deserialize_json(
            data["Status"]
        )
    if "StatusReason" in data:
        import capo_pca_connector_scep.types.connector_status_reason

        out["status_reason"] = (
            capo_pca_connector_scep.types.connector_status_reason.deserialize_json(
                data["StatusReason"]
            )
        )
    if "Endpoint" in data:
        out["endpoint"] = data["Endpoint"]
    if "CreatedAt" in data:
        import capo_pca_connector_scep.types._prelude.timestamp

        out["created_at"] = (
            capo_pca_connector_scep.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    if "UpdatedAt" in data:
        import capo_pca_connector_scep.types._prelude.timestamp

        out["updated_at"] = (
            capo_pca_connector_scep.types._prelude.timestamp.deserialize_json(
                data["UpdatedAt"]
            )
        )
    return out
