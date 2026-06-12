"""Generated from Smithy shape ``com.amazonaws.ssoadmin#Scopes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.scope_details

Scopes: TypeAlias = list["aws_sdk_sso_admin.types.scope_details.ScopeDetails"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Scopes) -> list:
    import aws_sdk_sso_admin.types.scope_details

    out: list = []
    for item in value:
        out.append(aws_sdk_sso_admin.types.scope_details.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Scopes:
    import aws_sdk_sso_admin.types.scope_details

    out: Scopes = []
    for item in data:
        out.append(aws_sdk_sso_admin.types.scope_details.deserialize_aws_json_1_1(item))
    return out
