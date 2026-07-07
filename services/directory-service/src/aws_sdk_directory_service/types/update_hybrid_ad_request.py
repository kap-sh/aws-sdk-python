"""Generated from Smithy shape ``com.amazonaws.directoryservice#UpdateHybridADRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.directory_id
    import aws_sdk_directory_service.types.hybrid_administrator_account_update
    import aws_sdk_directory_service.types.hybrid_customer_instances_settings


class UpdateHybridADRequest(TypedDict, closed=True):
    directory_id: "aws_sdk_directory_service.types.directory_id.DirectoryId"
    """<p>The identifier of the hybrid directory to update.</p>"""
    hybrid_administrator_account_update: NotRequired[
        "aws_sdk_directory_service.types.hybrid_administrator_account_update.HybridAdministratorAccountUpdate"
    ]
    """<p>We create a hybrid directory administrator account when we create a hybrid directory. Use <code>HybridAdministratorAccountUpdate</code> to recover the hybrid directory administrator account if you have deleted it.</p> <p>To recover your hybrid directory administrator account, we need temporary access to a user in your self-managed AD with administrator permissions in the form of a secret from Amazon Web Services Secrets Manager. We use these credentials once during recovery and don't store them.</p> <p>If your hybrid directory administrator account exists, then you don’t need to use <code>HybridAdministratorAccountUpdate</code>, even if you have updated your self-managed AD administrator user.</p>"""
    self_managed_instances_settings: NotRequired[
        "aws_sdk_directory_service.types.hybrid_customer_instances_settings.HybridCustomerInstancesSettings"
    ]
    """<p>Updates to the self-managed AD configuration, including DNS server IP addresses and Amazon Web Services System Manager managed node identifiers.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateHybridADRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    if "hybrid_administrator_account_update" in value:
        import aws_sdk_directory_service.types.hybrid_administrator_account_update

        out["HybridAdministratorAccountUpdate"] = (
            aws_sdk_directory_service.types.hybrid_administrator_account_update.serialize_aws_json_1_1(
                value["hybrid_administrator_account_update"]
            )
        )
    if "self_managed_instances_settings" in value:
        import aws_sdk_directory_service.types.hybrid_customer_instances_settings

        out["SelfManagedInstancesSettings"] = (
            aws_sdk_directory_service.types.hybrid_customer_instances_settings.serialize_aws_json_1_1(
                value["self_managed_instances_settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateHybridADRequest:
    out: UpdateHybridADRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError("UpdateHybridADRequest.directory_id required")
    if "HybridAdministratorAccountUpdate" in data:
        import aws_sdk_directory_service.types.hybrid_administrator_account_update

        out["hybrid_administrator_account_update"] = (
            aws_sdk_directory_service.types.hybrid_administrator_account_update.deserialize_aws_json_1_1(
                data["HybridAdministratorAccountUpdate"]
            )
        )
    if "SelfManagedInstancesSettings" in data:
        import aws_sdk_directory_service.types.hybrid_customer_instances_settings

        out["self_managed_instances_settings"] = (
            aws_sdk_directory_service.types.hybrid_customer_instances_settings.deserialize_aws_json_1_1(
                data["SelfManagedInstancesSettings"]
            )
        )
    return out
