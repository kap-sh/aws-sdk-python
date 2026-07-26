"""Generated from Smithy shape ``com.amazonaws.codecommit#SubModuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecommit.types.sub_module

SubModuleList: TypeAlias = list["capo_codecommit.types.sub_module.SubModule"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubModuleList) -> list:
    import capo_codecommit.types.sub_module

    out: list = []
    for item in value:
        out.append(capo_codecommit.types.sub_module.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SubModuleList:
    import capo_codecommit.types.sub_module

    out: SubModuleList = []
    for item in data:
        out.append(capo_codecommit.types.sub_module.deserialize_aws_json_1_1(item))
    return out
