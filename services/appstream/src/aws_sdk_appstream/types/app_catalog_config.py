"""Generated from Smithy shape ``com.amazonaws.appstream#AppCatalogConfig``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appstream.types.application_config

AppCatalogConfig: TypeAlias = list[
    "aws_sdk_appstream.types.application_config.ApplicationConfig"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppCatalogConfig) -> list:
    import aws_sdk_appstream.types.application_config

    out: list = []
    for item in value:
        out.append(
            aws_sdk_appstream.types.application_config.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AppCatalogConfig:
    import aws_sdk_appstream.types.application_config

    out: AppCatalogConfig = []
    for item in data:
        out.append(
            aws_sdk_appstream.types.application_config.deserialize_aws_json_1_1(item)
        )
    return out
