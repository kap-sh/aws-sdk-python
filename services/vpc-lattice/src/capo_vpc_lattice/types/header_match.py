"""Generated from Smithy shape ``com.amazonaws.vpclattice#HeaderMatch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_vpc_lattice.errors import DeserializationError

if TYPE_CHECKING:
    import capo_vpc_lattice.types.boolean
    import capo_vpc_lattice.types.header_match_name
    import capo_vpc_lattice.types.header_match_type


class HeaderMatch(TypedDict, closed=True):
    name: "capo_vpc_lattice.types.header_match_name.HeaderMatchName"
    """<p>The name of the header.</p>"""
    match: "capo_vpc_lattice.types.header_match_type.HeaderMatchType"
    """<p>The header match type.</p>"""
    case_sensitive: NotRequired["capo_vpc_lattice.types.boolean.Boolean"]
    """<p>Indicates whether the match is case sensitive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HeaderMatch) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_vpc_lattice.types.header_match_type

    out["match"] = capo_vpc_lattice.types.header_match_type.serialize_json(
        value["match"]
    )
    if "case_sensitive" in value:
        out["caseSensitive"] = value["case_sensitive"]
    return out


def deserialize_json(data: dict) -> HeaderMatch:
    out: HeaderMatch = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("HeaderMatch.name required")
    if "match" in data:
        import capo_vpc_lattice.types.header_match_type

        out["match"] = capo_vpc_lattice.types.header_match_type.deserialize_json(
            data["match"]
        )
    else:
        raise DeserializationError("HeaderMatch.match required")
    if "caseSensitive" in data:
        out["case_sensitive"] = data["caseSensitive"]
    return out
