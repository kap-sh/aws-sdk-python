"""Generated from Smithy shape ``com.amazonaws.kendra#SlackEntityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.slack_entity

SlackEntityList: TypeAlias = list["capo_kendra.types.slack_entity.SlackEntity"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SlackEntityList) -> list:
    import capo_kendra.types.slack_entity

    out: list = []
    for item in value:
        out.append(capo_kendra.types.slack_entity.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SlackEntityList:
    import capo_kendra.types.slack_entity

    out: SlackEntityList = []
    for item in data:
        out.append(capo_kendra.types.slack_entity.deserialize_aws_json_1_1(item))
    return out
