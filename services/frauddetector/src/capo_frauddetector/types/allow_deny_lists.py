"""Generated from Smithy shape ``com.amazonaws.frauddetector#AllowDenyLists``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.allow_deny_list

AllowDenyLists: TypeAlias = list[
    "capo_frauddetector.types.allow_deny_list.AllowDenyList"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AllowDenyLists) -> list:
    import capo_frauddetector.types.allow_deny_list

    out: list = []
    for item in value:
        out.append(
            capo_frauddetector.types.allow_deny_list.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AllowDenyLists:
    import capo_frauddetector.types.allow_deny_list

    out: AllowDenyLists = []
    for item in data:
        out.append(
            capo_frauddetector.types.allow_deny_list.deserialize_aws_json_1_1(item)
        )
    return out
