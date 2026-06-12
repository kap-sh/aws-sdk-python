"""Generated from Smithy shape ``com.amazonaws.lakeformation#LFTagErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.lf_tag_error

LFTagErrors: TypeAlias = list["aws_sdk_lakeformation.types.lf_tag_error.LFTagError"]


# --- restJson1 ser/de ---
def serialize_json(value: LFTagErrors) -> list:
    import aws_sdk_lakeformation.types.lf_tag_error

    out: list = []
    for item in value:
        out.append(aws_sdk_lakeformation.types.lf_tag_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> LFTagErrors:
    import aws_sdk_lakeformation.types.lf_tag_error

    out: LFTagErrors = []
    for item in data:
        out.append(aws_sdk_lakeformation.types.lf_tag_error.deserialize_json(item))
    return out
