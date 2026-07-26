"""Generated from Smithy shape ``com.amazonaws.emr#SessionStateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr.types.session_state

SessionStateList: TypeAlias = list["capo_emr.types.session_state.SessionState"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionStateList) -> list:
    import capo_emr.types.session_state

    out: list = []
    for item in value:
        out.append(capo_emr.types.session_state.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SessionStateList:
    import capo_emr.types.session_state

    out: SessionStateList = []
    for item in data:
        out.append(capo_emr.types.session_state.deserialize_aws_json_1_1(item))
    return out
