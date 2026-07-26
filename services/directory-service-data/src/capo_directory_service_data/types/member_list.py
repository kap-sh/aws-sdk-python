"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#MemberList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service_data.types.member

MemberList: TypeAlias = list["capo_directory_service_data.types.member.Member"]


# --- restJson1 ser/de ---
def serialize_json(value: MemberList) -> list:
    import capo_directory_service_data.types.member

    out: list = []
    for item in value:
        out.append(capo_directory_service_data.types.member.serialize_json(item))
    return out


def deserialize_json(data: list) -> MemberList:
    import capo_directory_service_data.types.member

    out: MemberList = []
    for item in data:
        out.append(capo_directory_service_data.types.member.deserialize_json(item))
    return out
