"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AssetListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.asset_type

AssetListType: TypeAlias = list[
    "capo_cognito_identity_provider.types.asset_type.AssetType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssetListType) -> list:
    import capo_cognito_identity_provider.types.asset_type

    out: list = []
    for item in value:
        out.append(
            capo_cognito_identity_provider.types.asset_type.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AssetListType:
    import capo_cognito_identity_provider.types.asset_type

    out: AssetListType = []
    for item in data:
        out.append(
            capo_cognito_identity_provider.types.asset_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
