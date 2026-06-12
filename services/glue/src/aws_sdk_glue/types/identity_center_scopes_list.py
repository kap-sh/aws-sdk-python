"""Generated from Smithy shape ``com.amazonaws.glue#IdentityCenterScopesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.identity_center_scope

IdentityCenterScopesList: TypeAlias = list[
    "aws_sdk_glue.types.identity_center_scope.IdentityCenterScope"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdentityCenterScopesList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> IdentityCenterScopesList:
    return list(data)
