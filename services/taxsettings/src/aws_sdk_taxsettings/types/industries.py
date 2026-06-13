"""Generated from Smithy shape ``com.amazonaws.taxsettings#Industries``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_taxsettings.errors import DeserializationError

Industries: TypeAlias = Literal[
    "CirculatingOrg",
    "ProfessionalOrg",
    "Banks",
    "Insurance",
    "PensionAndBenefitFunds",
    "DevelopmentAgencies",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CirculatingOrg",
        "ProfessionalOrg",
        "Banks",
        "Insurance",
        "PensionAndBenefitFunds",
        "DevelopmentAgencies",
    )
)


def serialize_json(value: Industries) -> str:
    return value


def deserialize_json(data: str) -> Industries:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Industries value: {data!r}")
    return cast(Industries, data)
