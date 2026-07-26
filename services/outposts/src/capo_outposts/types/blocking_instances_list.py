"""Generated from Smithy shape ``com.amazonaws.outposts#BlockingInstancesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_outposts.types.blocking_instance

BlockingInstancesList: TypeAlias = list[
    "capo_outposts.types.blocking_instance.BlockingInstance"
]


# --- restJson1 ser/de ---
def serialize_json(value: BlockingInstancesList) -> list:
    import capo_outposts.types.blocking_instance

    out: list = []
    for item in value:
        out.append(capo_outposts.types.blocking_instance.serialize_json(item))
    return out


def deserialize_json(data: list) -> BlockingInstancesList:
    import capo_outposts.types.blocking_instance

    out: BlockingInstancesList = []
    for item in data:
        out.append(capo_outposts.types.blocking_instance.deserialize_json(item))
    return out
