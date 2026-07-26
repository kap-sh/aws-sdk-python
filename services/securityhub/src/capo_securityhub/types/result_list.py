"""Generated from Smithy shape ``com.amazonaws.securityhub#ResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.result

ResultList: TypeAlias = list["capo_securityhub.types.result.Result"]


# --- restJson1 ser/de ---
def serialize_json(value: ResultList) -> list:
    import capo_securityhub.types.result

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.result.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResultList:
    import capo_securityhub.types.result

    out: ResultList = []
    for item in data:
        out.append(capo_securityhub.types.result.deserialize_json(item))
    return out
