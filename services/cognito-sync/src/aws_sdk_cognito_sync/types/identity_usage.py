"""Generated from Smithy shape ``com.amazonaws.cognitosync#IdentityUsage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cognito_sync.types.date
    import aws_sdk_cognito_sync.types.identity_id
    import aws_sdk_cognito_sync.types.identity_pool_id
    import aws_sdk_cognito_sync.types.integer
    import aws_sdk_cognito_sync.types.long


class IdentityUsage(TypedDict):
    identity_id: NotRequired["aws_sdk_cognito_sync.types.identity_id.IdentityId"]
    """A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region."""
    identity_pool_id: NotRequired[
        "aws_sdk_cognito_sync.types.identity_pool_id.IdentityPoolId"
    ]
    """A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region."""
    last_modified_date: NotRequired["aws_sdk_cognito_sync.types.date.Date"]
    """Date on which the identity was last modified."""
    dataset_count: "aws_sdk_cognito_sync.types.integer.Integer"
    """Number of datasets for the identity."""
    data_storage: NotRequired["aws_sdk_cognito_sync.types.long.Long"]
    """Total data storage for this identity."""


# --- restJson1 ser/de ---
def serialize_json(value: IdentityUsage) -> dict:
    out: dict = {}
    if "identity_id" in value:
        out["IdentityId"] = value["identity_id"]
    if "identity_pool_id" in value:
        out["IdentityPoolId"] = value["identity_pool_id"]
    if "last_modified_date" in value:
        import aws_sdk_cognito_sync.types.date

        out["LastModifiedDate"] = aws_sdk_cognito_sync.types.date.serialize_json(
            value["last_modified_date"]
        )
    out["DatasetCount"] = value.get("dataset_count", 0)
    if "data_storage" in value:
        out["DataStorage"] = value["data_storage"]
    return out


def deserialize_json(data: dict) -> IdentityUsage:
    out: IdentityUsage = {}  # type: ignore[typeddict-item]
    if "IdentityId" in data:
        out["identity_id"] = data["IdentityId"]
    if "IdentityPoolId" in data:
        out["identity_pool_id"] = data["IdentityPoolId"]
    if "LastModifiedDate" in data:
        import aws_sdk_cognito_sync.types.date

        out["last_modified_date"] = aws_sdk_cognito_sync.types.date.deserialize_json(
            data["LastModifiedDate"]
        )
    if "DatasetCount" in data:
        out["dataset_count"] = data["DatasetCount"]
    else:
        out["dataset_count"] = 0
    if "DataStorage" in data:
        out["data_storage"] = data["DataStorage"]
    return out
