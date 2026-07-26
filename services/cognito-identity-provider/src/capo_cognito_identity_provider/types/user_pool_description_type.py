"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UserPoolDescriptionType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.date_type
    import capo_cognito_identity_provider.types.lambda_config_type
    import capo_cognito_identity_provider.types.replica_regions_type
    import capo_cognito_identity_provider.types.status_type
    import capo_cognito_identity_provider.types.user_pool_id_type
    import capo_cognito_identity_provider.types.user_pool_name_type


class UserPoolDescriptionType(TypedDict, closed=True):
    id: NotRequired[
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    ]
    """<p>The user pool ID.</p>"""
    name: NotRequired[
        "capo_cognito_identity_provider.types.user_pool_name_type.UserPoolNameType"
    ]
    """<p>The user pool name.</p>"""
    lambda_config: NotRequired[
        "capo_cognito_identity_provider.types.lambda_config_type.LambdaConfigType"
    ]
    """<p>A collection of user pool Lambda triggers. Amazon Cognito invokes triggers at several possible stages of user pool operations. Triggers can modify the outcome of the operations that invoked them.</p>"""
    status: NotRequired["capo_cognito_identity_provider.types.status_type.StatusType"]
    """<p>The user pool status.</p>"""
    last_modified_date: NotRequired[
        "capo_cognito_identity_provider.types.date_type.DateType"
    ]
    """<p>The date and time when the item was modified. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java <code>Date</code> object.</p>"""
    creation_date: NotRequired[
        "capo_cognito_identity_provider.types.date_type.DateType"
    ]
    """<p>The date and time when the item was created. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java <code>Date</code> object.</p>"""
    replica_regions: NotRequired[
        "capo_cognito_identity_provider.types.replica_regions_type.ReplicaRegionsType"
    ]
    """<p>A list of Amazon Web Services Regions where replicas of this user pool exist.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserPoolDescriptionType) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "lambda_config" in value:
        import capo_cognito_identity_provider.types.lambda_config_type

        out["LambdaConfig"] = (
            capo_cognito_identity_provider.types.lambda_config_type.serialize_aws_json_1_1(
                value["lambda_config"]
            )
        )
    if "status" in value:
        import capo_cognito_identity_provider.types.status_type

        out["Status"] = (
            capo_cognito_identity_provider.types.status_type.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "last_modified_date" in value:
        import capo_cognito_identity_provider.types.date_type

        out["LastModifiedDate"] = (
            capo_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
                value["last_modified_date"]
            )
        )
    if "creation_date" in value:
        import capo_cognito_identity_provider.types.date_type

        out["CreationDate"] = (
            capo_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
                value["creation_date"]
            )
        )
    if "replica_regions" in value:
        import capo_cognito_identity_provider.types.replica_regions_type

        out["ReplicaRegions"] = (
            capo_cognito_identity_provider.types.replica_regions_type.serialize_aws_json_1_1(
                value["replica_regions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UserPoolDescriptionType:
    out: UserPoolDescriptionType = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "LambdaConfig" in data:
        import capo_cognito_identity_provider.types.lambda_config_type

        out["lambda_config"] = (
            capo_cognito_identity_provider.types.lambda_config_type.deserialize_aws_json_1_1(
                data["LambdaConfig"]
            )
        )
    if "Status" in data:
        import capo_cognito_identity_provider.types.status_type

        out["status"] = (
            capo_cognito_identity_provider.types.status_type.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "LastModifiedDate" in data:
        import capo_cognito_identity_provider.types.date_type

        out["last_modified_date"] = (
            capo_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["LastModifiedDate"]
            )
        )
    if "CreationDate" in data:
        import capo_cognito_identity_provider.types.date_type

        out["creation_date"] = (
            capo_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["CreationDate"]
            )
        )
    if "ReplicaRegions" in data:
        import capo_cognito_identity_provider.types.replica_regions_type

        out["replica_regions"] = (
            capo_cognito_identity_provider.types.replica_regions_type.deserialize_aws_json_1_1(
                data["ReplicaRegions"]
            )
        )
    return out
