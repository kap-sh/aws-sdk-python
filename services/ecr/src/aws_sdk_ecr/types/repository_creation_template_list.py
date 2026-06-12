"""Generated from Smithy shape ``com.amazonaws.ecr#RepositoryCreationTemplateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecr.types.repository_creation_template

RepositoryCreationTemplateList: TypeAlias = list[
    "aws_sdk_ecr.types.repository_creation_template.RepositoryCreationTemplate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryCreationTemplateList) -> list:
    import aws_sdk_ecr.types.repository_creation_template

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ecr.types.repository_creation_template.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RepositoryCreationTemplateList:
    import aws_sdk_ecr.types.repository_creation_template

    out: RepositoryCreationTemplateList = []
    for item in data:
        out.append(
            aws_sdk_ecr.types.repository_creation_template.deserialize_aws_json_1_1(
                item
            )
        )
    return out
