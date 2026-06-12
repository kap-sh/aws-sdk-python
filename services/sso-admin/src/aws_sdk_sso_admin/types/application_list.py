"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ApplicationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.application

ApplicationList: TypeAlias = list["aws_sdk_sso_admin.types.application.Application"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationList) -> list:
    import aws_sdk_sso_admin.types.application

    out: list = []
    for item in value:
        out.append(aws_sdk_sso_admin.types.application.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ApplicationList:
    import aws_sdk_sso_admin.types.application

    out: ApplicationList = []
    for item in data:
        out.append(aws_sdk_sso_admin.types.application.deserialize_aws_json_1_1(item))
    return out
