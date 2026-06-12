"""Generated from Smithy shape ``com.amazonaws.codedeploy#RevisionInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.revision_info

RevisionInfoList: TypeAlias = list[
    "aws_sdk_codedeploy.types.revision_info.RevisionInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RevisionInfoList) -> list:
    import aws_sdk_codedeploy.types.revision_info

    out: list = []
    for item in value:
        out.append(aws_sdk_codedeploy.types.revision_info.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RevisionInfoList:
    import aws_sdk_codedeploy.types.revision_info

    out: RevisionInfoList = []
    for item in data:
        out.append(
            aws_sdk_codedeploy.types.revision_info.deserialize_aws_json_1_1(item)
        )
    return out
