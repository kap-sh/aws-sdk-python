"""Generated from Smithy shape ``com.amazonaws.connect#UseCaseSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.use_case

UseCaseSummaryList: TypeAlias = list["aws_sdk_connect.types.use_case.UseCase"]


# --- restJson1 ser/de ---
def serialize_json(value: UseCaseSummaryList) -> list:
    import aws_sdk_connect.types.use_case

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.use_case.serialize_json(item))
    return out


def deserialize_json(data: list) -> UseCaseSummaryList:
    import aws_sdk_connect.types.use_case

    out: UseCaseSummaryList = []
    for item in data:
        out.append(aws_sdk_connect.types.use_case.deserialize_json(item))
    return out
