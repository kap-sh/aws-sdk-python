"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#ServicePrincipalName``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_pca_connector_ad.types.connector_arn
    import aws_sdk_pca_connector_ad.types.directory_registration_arn
    import aws_sdk_pca_connector_ad.types.service_principal_name_status
    import aws_sdk_pca_connector_ad.types.service_principal_name_status_reason


class ServicePrincipalName(TypedDict):
    directory_registration_arn: NotRequired[
        "aws_sdk_pca_connector_ad.types.directory_registration_arn.DirectoryRegistrationArn"
    ]
    r"""<p>The Amazon Resource Name (ARN) that was returned when you called <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html\">CreateDirectoryRegistration</a>.</p>"""
    connector_arn: NotRequired[
        "aws_sdk_pca_connector_ad.types.connector_arn.ConnectorArn"
    ]
    r"""<p>The Amazon Resource Name (ARN) that was returned when you called <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html\">CreateConnector.html</a>.</p>"""
    status: NotRequired[
        "aws_sdk_pca_connector_ad.types.service_principal_name_status.ServicePrincipalNameStatus"
    ]
    """<p>The status of a service principal name.</p>"""
    status_reason: NotRequired[
        "aws_sdk_pca_connector_ad.types.service_principal_name_status_reason.ServicePrincipalNameStatusReason"
    ]
    """<p>Additional information for the status of a service principal name if the status is failed.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the service principal name was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the service principal name was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServicePrincipalName) -> dict:
    out: dict = {}
    if "directory_registration_arn" in value:
        out["DirectoryRegistrationArn"] = value["directory_registration_arn"]
    if "connector_arn" in value:
        out["ConnectorArn"] = value["connector_arn"]
    if "status" in value:
        import aws_sdk_pca_connector_ad.types.service_principal_name_status

        out["Status"] = (
            aws_sdk_pca_connector_ad.types.service_principal_name_status.serialize_json(
                value["status"]
            )
        )
    if "status_reason" in value:
        import aws_sdk_pca_connector_ad.types.service_principal_name_status_reason

        out["StatusReason"] = (
            aws_sdk_pca_connector_ad.types.service_principal_name_status_reason.serialize_json(
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


def deserialize_json(data: dict) -> ServicePrincipalName:
    out: ServicePrincipalName = {}  # type: ignore[typeddict-item]
    if "DirectoryRegistrationArn" in data:
        out["directory_registration_arn"] = data["DirectoryRegistrationArn"]
    if "ConnectorArn" in data:
        out["connector_arn"] = data["ConnectorArn"]
    if "Status" in data:
        import aws_sdk_pca_connector_ad.types.service_principal_name_status

        out["status"] = (
            aws_sdk_pca_connector_ad.types.service_principal_name_status.deserialize_json(
                data["Status"]
            )
        )
    if "StatusReason" in data:
        import aws_sdk_pca_connector_ad.types.service_principal_name_status_reason

        out["status_reason"] = (
            aws_sdk_pca_connector_ad.types.service_principal_name_status_reason.deserialize_json(
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
