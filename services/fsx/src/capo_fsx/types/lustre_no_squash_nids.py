"""Generated from Smithy shape ``com.amazonaws.fsx#LustreNoSquashNids``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fsx.types.lustre_no_squash_nid

LustreNoSquashNids: TypeAlias = list[
    "capo_fsx.types.lustre_no_squash_nid.LustreNoSquashNid"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LustreNoSquashNids) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> LustreNoSquashNids:
    return list(data)
