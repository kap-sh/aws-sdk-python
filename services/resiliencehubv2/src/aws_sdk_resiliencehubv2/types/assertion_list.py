"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#AssertionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.assertion

AssertionList: TypeAlias = list["aws_sdk_resiliencehubv2.types.assertion.Assertion"]


# --- restJson1 ser/de ---
def serialize_json(value: AssertionList) -> list:
    import aws_sdk_resiliencehubv2.types.assertion

    out: list = []
    for item in value:
        out.append(aws_sdk_resiliencehubv2.types.assertion.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssertionList:
    import aws_sdk_resiliencehubv2.types.assertion

    out: AssertionList = []
    for item in data:
        out.append(aws_sdk_resiliencehubv2.types.assertion.deserialize_json(item))
    return out
