"""Generated from Smithy shape ``com.amazonaws.snowball#DependentServiceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_snowball.types.dependent_service

DependentServiceList: TypeAlias = list[
    "aws_sdk_snowball.types.dependent_service.DependentService"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DependentServiceList) -> list:
    import aws_sdk_snowball.types.dependent_service

    out: list = []
    for item in value:
        out.append(
            aws_sdk_snowball.types.dependent_service.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DependentServiceList:
    import aws_sdk_snowball.types.dependent_service

    out: DependentServiceList = []
    for item in data:
        out.append(
            aws_sdk_snowball.types.dependent_service.deserialize_aws_json_1_1(item)
        )
    return out
