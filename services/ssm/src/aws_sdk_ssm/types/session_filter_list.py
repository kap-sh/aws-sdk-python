"""Generated from Smithy shape ``com.amazonaws.ssm#SessionFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.session_filter

SessionFilterList: TypeAlias = list["aws_sdk_ssm.types.session_filter.SessionFilter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionFilterList) -> list:
    import aws_sdk_ssm.types.session_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.session_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SessionFilterList:
    import aws_sdk_ssm.types.session_filter

    out: SessionFilterList = []
    for item in data:
        out.append(aws_sdk_ssm.types.session_filter.deserialize_aws_json_1_1(item))
    return out
