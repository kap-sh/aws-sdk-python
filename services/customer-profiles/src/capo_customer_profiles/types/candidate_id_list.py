"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CandidateIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.string1_to255

CandidateIdList: TypeAlias = list[
    "capo_customer_profiles.types.string1_to255.string1To255"
]


# --- restJson1 ser/de ---
def serialize_json(value: CandidateIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> CandidateIdList:
    return list(data)
