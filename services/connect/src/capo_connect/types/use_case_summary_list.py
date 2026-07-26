"""Generated from Smithy shape ``com.amazonaws.connect#UseCaseSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.use_case

UseCaseSummaryList: TypeAlias = list["capo_connect.types.use_case.UseCase"]


# --- restJson1 ser/de ---
def serialize_json(value: UseCaseSummaryList) -> list:
    import capo_connect.types.use_case

    out: list = []
    for item in value:
        out.append(capo_connect.types.use_case.serialize_json(item))
    return out


def deserialize_json(data: list) -> UseCaseSummaryList:
    import capo_connect.types.use_case

    out: UseCaseSummaryList = []
    for item in data:
        out.append(capo_connect.types.use_case.deserialize_json(item))
    return out
