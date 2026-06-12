"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.association_version_info

AssociationVersionList: TypeAlias = list[
    "aws_sdk_ssm.types.association_version_info.AssociationVersionInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationVersionList) -> list:
    import aws_sdk_ssm.types.association_version_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm.types.association_version_info.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AssociationVersionList:
    import aws_sdk_ssm.types.association_version_info

    out: AssociationVersionList = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.association_version_info.deserialize_aws_json_1_1(item)
        )
    return out
