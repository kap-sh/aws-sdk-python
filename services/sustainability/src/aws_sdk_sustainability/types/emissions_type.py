"""Generated from Smithy shape ``com.amazonaws.sustainability#EmissionsType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sustainability.errors import DeserializationError

"""<p>Specifies the types of carbon emissions calculations available.</p>"""
EmissionsType: TypeAlias = Literal[
    "TOTAL_LBM_CARBON_EMISSIONS",
    "TOTAL_MBM_CARBON_EMISSIONS",
    "TOTAL_SCOPE_1_CARBON_EMISSIONS",
    "TOTAL_SCOPE_2_LBM_CARBON_EMISSIONS",
    "TOTAL_SCOPE_2_MBM_CARBON_EMISSIONS",
    "TOTAL_SCOPE_3_LBM_CARBON_EMISSIONS",
    "TOTAL_SCOPE_3_MBM_CARBON_EMISSIONS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TOTAL_LBM_CARBON_EMISSIONS",
        "TOTAL_MBM_CARBON_EMISSIONS",
        "TOTAL_SCOPE_1_CARBON_EMISSIONS",
        "TOTAL_SCOPE_2_LBM_CARBON_EMISSIONS",
        "TOTAL_SCOPE_2_MBM_CARBON_EMISSIONS",
        "TOTAL_SCOPE_3_LBM_CARBON_EMISSIONS",
        "TOTAL_SCOPE_3_MBM_CARBON_EMISSIONS",
    )
)


def serialize_json(value: EmissionsType) -> str:
    return value


def deserialize_json(data: str) -> EmissionsType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EmissionsType value: {data!r}")
    return cast(EmissionsType, data)
