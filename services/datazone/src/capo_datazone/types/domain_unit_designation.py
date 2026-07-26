"""Generated from Smithy shape ``com.amazonaws.datazone#DomainUnitDesignation``."""

from typing import Literal, TypeAlias, cast

DomainUnitDesignation: TypeAlias = Literal["OWNER",]


# --- restJson1 ser/de ---
def serialize_json(value: DomainUnitDesignation) -> str:
    return value


def deserialize_json(data: str) -> DomainUnitDesignation:
    return cast(DomainUnitDesignation, data)
