"""Generated from Smithy shape ``com.amazonaws.vpclattice#Matcher``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_vpc_lattice.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_vpc_lattice.types.http_code_matcher


class _Matcher_httpCode(TypedDict, closed=True):
    httpCode: "capo_vpc_lattice.types.http_code_matcher.HttpCodeMatcher"


Matcher: TypeAlias = _Matcher_httpCode


# --- restJson1 ser/de ---
def serialize_json(value: Matcher) -> dict:
    if "httpCode" in value:
        return {"httpCode": value["httpCode"]}
    else:
        raise SerializationError("Matcher: no variant present")


def deserialize_json(data: dict) -> Matcher:
    if "httpCode" in data:
        return {"httpCode": data["httpCode"]}
    else:
        raise DeserializationError("Matcher: no recognized variant key")
