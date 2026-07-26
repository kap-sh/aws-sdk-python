"""Generated from Smithy shape ``com.amazonaws.codedeploy#ApplicationsInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codedeploy.types.application_info

ApplicationsInfoList: TypeAlias = list[
    "capo_codedeploy.types.application_info.ApplicationInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationsInfoList) -> list:
    import capo_codedeploy.types.application_info

    out: list = []
    for item in value:
        out.append(capo_codedeploy.types.application_info.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ApplicationsInfoList:
    import capo_codedeploy.types.application_info

    out: ApplicationsInfoList = []
    for item in data:
        out.append(
            capo_codedeploy.types.application_info.deserialize_aws_json_1_1(item)
        )
    return out
