"""Generated from Smithy shape ``com.amazonaws.vpclattice#RuleMatch``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_vpc_lattice.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_vpc_lattice.types.http_match


class _RuleMatch_httpMatch(TypedDict, closed=True):
    httpMatch: "capo_vpc_lattice.types.http_match.HttpMatch"


RuleMatch: TypeAlias = _RuleMatch_httpMatch


# --- restJson1 ser/de ---
def serialize_json(value: RuleMatch) -> dict:
    if "httpMatch" in value:
        import capo_vpc_lattice.types.http_match

        return {
            "httpMatch": capo_vpc_lattice.types.http_match.serialize_json(
                value["httpMatch"]
            )
        }
    else:
        raise SerializationError("RuleMatch: no variant present")


def deserialize_json(data: dict) -> RuleMatch:
    if "httpMatch" in data:
        import capo_vpc_lattice.types.http_match

        return {
            "httpMatch": capo_vpc_lattice.types.http_match.deserialize_json(
                data["httpMatch"]
            )
        }
    else:
        raise DeserializationError("RuleMatch: no recognized variant key")
