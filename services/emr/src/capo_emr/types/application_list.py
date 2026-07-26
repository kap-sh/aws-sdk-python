"""Generated from Smithy shape ``com.amazonaws.emr#ApplicationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr.types.application

ApplicationList: TypeAlias = list["capo_emr.types.application.Application"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationList) -> list:
    import capo_emr.types.application

    out: list = []
    for item in value:
        out.append(capo_emr.types.application.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ApplicationList:
    import capo_emr.types.application

    out: ApplicationList = []
    for item in data:
        out.append(capo_emr.types.application.deserialize_aws_json_1_1(item))
    return out
