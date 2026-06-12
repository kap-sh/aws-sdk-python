"""Generated from Smithy shape ``com.amazonaws.kendraranking#DocumentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra_ranking.types.document

DocumentList: TypeAlias = list["aws_sdk_kendra_ranking.types.document.Document"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DocumentList) -> list:
    import aws_sdk_kendra_ranking.types.document

    out: list = []
    for item in value:
        out.append(aws_sdk_kendra_ranking.types.document.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> DocumentList:
    import aws_sdk_kendra_ranking.types.document

    out: DocumentList = []
    for item in data:
        out.append(aws_sdk_kendra_ranking.types.document.deserialize_aws_json_1_0(item))
    return out
