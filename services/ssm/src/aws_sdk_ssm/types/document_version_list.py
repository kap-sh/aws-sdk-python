"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.document_version_info

DocumentVersionList: TypeAlias = list[
    "aws_sdk_ssm.types.document_version_info.DocumentVersionInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentVersionList) -> list:
    import aws_sdk_ssm.types.document_version_info

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.document_version_info.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DocumentVersionList:
    import aws_sdk_ssm.types.document_version_info

    out: DocumentVersionList = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.document_version_info.deserialize_aws_json_1_1(item)
        )
    return out
