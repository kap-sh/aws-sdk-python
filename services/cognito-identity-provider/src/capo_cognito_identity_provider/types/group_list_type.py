"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GroupListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.group_type

GroupListType: TypeAlias = list[
    "capo_cognito_identity_provider.types.group_type.GroupType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GroupListType) -> list:
    import capo_cognito_identity_provider.types.group_type

    out: list = []
    for item in value:
        out.append(
            capo_cognito_identity_provider.types.group_type.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> GroupListType:
    import capo_cognito_identity_provider.types.group_type

    out: GroupListType = []
    for item in data:
        out.append(
            capo_cognito_identity_provider.types.group_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
