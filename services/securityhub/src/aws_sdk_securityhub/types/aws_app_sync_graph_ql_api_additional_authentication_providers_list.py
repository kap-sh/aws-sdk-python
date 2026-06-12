"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_additional_authentication_providers_details

AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_additional_authentication_providers_details.AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetails"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersList,
) -> list:
    import aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_additional_authentication_providers_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_additional_authentication_providers_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersList:
    import aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_additional_authentication_providers_details

    out: AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_additional_authentication_providers_details.deserialize_json(
                item
            )
        )
    return out
