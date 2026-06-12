"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ResourceServerScopes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.resource_server_scope
    import aws_sdk_sso_admin.types.resource_server_scope_details

ResourceServerScopes: TypeAlias = dict[
    "aws_sdk_sso_admin.types.resource_server_scope.ResourceServerScope",
    "aws_sdk_sso_admin.types.resource_server_scope_details.ResourceServerScopeDetails",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ResourceServerScopes) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_sso_admin.types.resource_server_scope_details

        out[key] = (
            aws_sdk_sso_admin.types.resource_server_scope_details.serialize_aws_json_1_1(
                value
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceServerScopes:
    out: ResourceServerScopes = {}
    for key, value in data.items():
        import aws_sdk_sso_admin.types.resource_server_scope_details

        out[key] = (
            aws_sdk_sso_admin.types.resource_server_scope_details.deserialize_aws_json_1_1(
                value
            )
        )
    return out
