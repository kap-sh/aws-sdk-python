"""Generated from Smithy shape ``com.amazonaws.vpclattice#PathMatchType``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_vpc_lattice.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.path_match_exact
    import aws_sdk_vpc_lattice.types.path_match_prefix


class _PathMatchType_exact(TypedDict, closed=True):
    exact: "aws_sdk_vpc_lattice.types.path_match_exact.PathMatchExact"


class _PathMatchType_prefix(TypedDict, closed=True):
    prefix: "aws_sdk_vpc_lattice.types.path_match_prefix.PathMatchPrefix"


PathMatchType: TypeAlias = _PathMatchType_exact | _PathMatchType_prefix


# --- restJson1 ser/de ---
def serialize_json(value: PathMatchType) -> dict:
    if "exact" in value:
        return {"exact": value["exact"]}
    elif "prefix" in value:
        return {"prefix": value["prefix"]}
    else:
        raise SerializationError("PathMatchType: no variant present")


def deserialize_json(data: dict) -> PathMatchType:
    if "exact" in data:
        return {"exact": data["exact"]}
    elif "prefix" in data:
        return {"prefix": data["prefix"]}
    else:
        raise DeserializationError("PathMatchType: no recognized variant key")
