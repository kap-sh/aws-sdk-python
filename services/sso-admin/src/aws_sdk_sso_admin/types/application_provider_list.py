"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ApplicationProviderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.application_provider

ApplicationProviderList: TypeAlias = list[
    "aws_sdk_sso_admin.types.application_provider.ApplicationProvider"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationProviderList) -> list:
    import aws_sdk_sso_admin.types.application_provider

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sso_admin.types.application_provider.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ApplicationProviderList:
    import aws_sdk_sso_admin.types.application_provider

    out: ApplicationProviderList = []
    for item in data:
        out.append(
            aws_sdk_sso_admin.types.application_provider.deserialize_aws_json_1_1(item)
        )
    return out
