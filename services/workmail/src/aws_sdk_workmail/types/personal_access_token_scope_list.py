"""Generated from Smithy shape ``com.amazonaws.workmail#PersonalAccessTokenScopeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workmail.types.personal_access_token_scope

PersonalAccessTokenScopeList: TypeAlias = list[
    "aws_sdk_workmail.types.personal_access_token_scope.PersonalAccessTokenScope"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PersonalAccessTokenScopeList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PersonalAccessTokenScopeList:
    return list(data)
