"""Generated from Smithy shape ``com.amazonaws.lakeformation#Expression``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.lf_tag

Expression: TypeAlias = list["aws_sdk_lakeformation.types.lf_tag.LFTag"]


# --- restJson1 ser/de ---
def serialize_json(value: Expression) -> list:
    import aws_sdk_lakeformation.types.lf_tag

    out: list = []
    for item in value:
        out.append(aws_sdk_lakeformation.types.lf_tag.serialize_json(item))
    return out


def deserialize_json(data: list) -> Expression:
    import aws_sdk_lakeformation.types.lf_tag

    out: Expression = []
    for item in data:
        out.append(aws_sdk_lakeformation.types.lf_tag.deserialize_json(item))
    return out
