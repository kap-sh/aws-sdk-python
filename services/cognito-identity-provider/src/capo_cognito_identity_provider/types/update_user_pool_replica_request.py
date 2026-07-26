"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UpdateUserPoolReplicaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.region_name_type
    import capo_cognito_identity_provider.types.update_replica_status_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class UpdateUserPoolReplicaRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that contains the replica to update.</p>"""
    region_name: "capo_cognito_identity_provider.types.region_name_type.RegionNameType"
    """<p>The Amazon Web Services Region of the replica to update.</p>"""
    status: "capo_cognito_identity_provider.types.update_replica_status_type.UpdateReplicaStatusType"
    """<p>The status to set for the replica. Valid values are ACTIVE and INACTIVE.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateUserPoolReplicaRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["RegionName"] = value["region_name"]
    import capo_cognito_identity_provider.types.update_replica_status_type

    out["Status"] = (
        capo_cognito_identity_provider.types.update_replica_status_type.serialize_aws_json_1_1(
            value["status"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateUserPoolReplicaRequest:
    out: UpdateUserPoolReplicaRequest = {}  # type: ignore[typeddict-item]
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError("UpdateUserPoolReplicaRequest.user_pool_id required")
    if "RegionName" in data:
        out["region_name"] = data["RegionName"]
    else:
        raise DeserializationError("UpdateUserPoolReplicaRequest.region_name required")
    if "Status" in data:
        import capo_cognito_identity_provider.types.update_replica_status_type

        out["status"] = (
            capo_cognito_identity_provider.types.update_replica_status_type.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("UpdateUserPoolReplicaRequest.status required")
    return out
