"""Generated from Smithy shape ``com.amazonaws.mediatailor#HttpPackageConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.http_package_configuration

HttpPackageConfigurations: TypeAlias = list[
    "aws_sdk_mediatailor.types.http_package_configuration.HttpPackageConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: HttpPackageConfigurations) -> list:
    import aws_sdk_mediatailor.types.http_package_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediatailor.types.http_package_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> HttpPackageConfigurations:
    import aws_sdk_mediatailor.types.http_package_configuration

    out: HttpPackageConfigurations = []
    for item in data:
        out.append(
            aws_sdk_mediatailor.types.http_package_configuration.deserialize_json(item)
        )
    return out
