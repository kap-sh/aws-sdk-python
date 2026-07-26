"""Generated from Smithy shape ``com.amazonaws.emr#SessionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr.types.session

SessionList: TypeAlias = list["capo_emr.types.session.Session"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionList) -> list:
    import capo_emr.types.session

    out: list = []
    for item in value:
        out.append(capo_emr.types.session.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SessionList:
    import capo_emr.types.session

    out: SessionList = []
    for item in data:
        out.append(capo_emr.types.session.deserialize_aws_json_1_1(item))
    return out
