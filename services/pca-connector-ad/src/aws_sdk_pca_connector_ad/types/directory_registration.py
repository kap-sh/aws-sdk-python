"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#DirectoryRegistration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_pca_connector_ad.types.directory_id
    import aws_sdk_pca_connector_ad.types.directory_registration_arn
    import aws_sdk_pca_connector_ad.types.directory_registration_status
    import aws_sdk_pca_connector_ad.types.directory_registration_status_reason


class DirectoryRegistration(TypedDict):
    arn: NotRequired[
        "aws_sdk_pca_connector_ad.types.directory_registration_arn.DirectoryRegistrationArn"
    ]
    """<p>The Amazon Resource Name (ARN) that was returned when you called CreateDirectoryRegistration. </p>"""
    directory_id: NotRequired["aws_sdk_pca_connector_ad.types.directory_id.DirectoryId"]
    """<p>The identifier of the Active Directory.</p>"""
    status: NotRequired[
        "aws_sdk_pca_connector_ad.types.directory_registration_status.DirectoryRegistrationStatus"
    ]
    """<p>Status of the directory registration.</p>"""
    status_reason: NotRequired[
        "aws_sdk_pca_connector_ad.types.directory_registration_status_reason.DirectoryRegistrationStatusReason"
    ]
    """<p>Additional information about the directory registration status if the status is failed.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the directory registration was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the directory registration was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DirectoryRegistration) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "status" in value:
        import aws_sdk_pca_connector_ad.types.directory_registration_status

        out["Status"] = (
            aws_sdk_pca_connector_ad.types.directory_registration_status.serialize_json(
                value["status"]
            )
        )
    if "status_reason" in value:
        import aws_sdk_pca_connector_ad.types.directory_registration_status_reason

        out["StatusReason"] = (
            aws_sdk_pca_connector_ad.types.directory_registration_status_reason.serialize_json(
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


def deserialize_json(data: dict) -> DirectoryRegistration:
    out: DirectoryRegistration = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    if "Status" in data:
        import aws_sdk_pca_connector_ad.types.directory_registration_status

        out["status"] = (
            aws_sdk_pca_connector_ad.types.directory_registration_status.deserialize_json(
                data["Status"]
            )
        )
    if "StatusReason" in data:
        import aws_sdk_pca_connector_ad.types.directory_registration_status_reason

        out["status_reason"] = (
            aws_sdk_pca_connector_ad.types.directory_registration_status_reason.deserialize_json(
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
