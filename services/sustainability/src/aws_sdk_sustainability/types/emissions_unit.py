"""Generated from Smithy shape ``com.amazonaws.sustainability#EmissionsUnit``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies the unit of measurement for emissions.</p>"""
EmissionsUnit: TypeAlias = Literal["MTCO2e",]


# --- restJson1 ser/de ---
def serialize_json(value: EmissionsUnit) -> str:
    return value


def deserialize_json(data: str) -> EmissionsUnit:
    return cast(EmissionsUnit, data)
