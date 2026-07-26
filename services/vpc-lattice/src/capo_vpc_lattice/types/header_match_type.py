"""Generated from Smithy shape ``com.amazonaws.vpclattice#HeaderMatchType``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_vpc_lattice.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_vpc_lattice.types.header_match_contains
    import capo_vpc_lattice.types.header_match_exact
    import capo_vpc_lattice.types.header_match_prefix


class _HeaderMatchType_exact(TypedDict, closed=True):
    exact: "capo_vpc_lattice.types.header_match_exact.HeaderMatchExact"


class _HeaderMatchType_prefix(TypedDict, closed=True):
    prefix: "capo_vpc_lattice.types.header_match_prefix.HeaderMatchPrefix"


class _HeaderMatchType_contains(TypedDict, closed=True):
    contains: "capo_vpc_lattice.types.header_match_contains.HeaderMatchContains"


HeaderMatchType: TypeAlias = (
    _HeaderMatchType_exact | _HeaderMatchType_prefix | _HeaderMatchType_contains
)


# --- restJson1 ser/de ---
def serialize_json(value: HeaderMatchType) -> dict:
    if "exact" in value:
        return {"exact": value["exact"]}
    elif "prefix" in value:
        return {"prefix": value["prefix"]}
    elif "contains" in value:
        return {"contains": value["contains"]}
    else:
        raise SerializationError("HeaderMatchType: no variant present")


def deserialize_json(data: dict) -> HeaderMatchType:
    if "exact" in data:
        return {"exact": data["exact"]}
    elif "prefix" in data:
        return {"prefix": data["prefix"]}
    elif "contains" in data:
        return {"contains": data["contains"]}
    else:
        raise DeserializationError("HeaderMatchType: no recognized variant key")
