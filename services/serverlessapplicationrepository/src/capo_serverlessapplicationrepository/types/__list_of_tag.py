"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#__listOfTag``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_serverlessapplicationrepository.types.tag

__listOfTag: TypeAlias = list["capo_serverlessapplicationrepository.types.tag.Tag"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfTag) -> list:
    import capo_serverlessapplicationrepository.types.tag

    out: list = []
    for item in value:
        out.append(capo_serverlessapplicationrepository.types.tag.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfTag:
    import capo_serverlessapplicationrepository.types.tag

    out: __listOfTag = []
    for item in data:
        out.append(
            capo_serverlessapplicationrepository.types.tag.deserialize_json(item)
        )
    return out
