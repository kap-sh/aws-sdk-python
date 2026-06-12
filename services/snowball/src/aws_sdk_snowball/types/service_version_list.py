"""Generated from Smithy shape ``com.amazonaws.snowball#ServiceVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_snowball.types.service_version

ServiceVersionList: TypeAlias = list[
    "aws_sdk_snowball.types.service_version.ServiceVersion"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceVersionList) -> list:
    import aws_sdk_snowball.types.service_version

    out: list = []
    for item in value:
        out.append(aws_sdk_snowball.types.service_version.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceVersionList:
    import aws_sdk_snowball.types.service_version

    out: ServiceVersionList = []
    for item in data:
        out.append(
            aws_sdk_snowball.types.service_version.deserialize_aws_json_1_1(item)
        )
    return out
