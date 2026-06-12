"""Generated from Smithy shape ``com.amazonaws.vpclattice#PathMatch``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_vpc_lattice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.boolean
    import aws_sdk_vpc_lattice.types.path_match_type


class PathMatch(TypedDict):
    match: "aws_sdk_vpc_lattice.types.path_match_type.PathMatchType"
    """<p>The type of path match.</p>"""
    case_sensitive: NotRequired["aws_sdk_vpc_lattice.types.boolean.Boolean"]
    """<p>Indicates whether the match is case sensitive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PathMatch) -> dict:
    out: dict = {}
    import aws_sdk_vpc_lattice.types.path_match_type

    out["match"] = aws_sdk_vpc_lattice.types.path_match_type.serialize_json(
        value["match"]
    )
    if "case_sensitive" in value:
        out["caseSensitive"] = value["case_sensitive"]
    return out


def deserialize_json(data: dict) -> PathMatch:
    out: PathMatch = {}  # type: ignore[typeddict-item]
    if "match" in data:
        import aws_sdk_vpc_lattice.types.path_match_type

        out["match"] = aws_sdk_vpc_lattice.types.path_match_type.deserialize_json(
            data["match"]
        )
    else:
        raise DeserializationError("PathMatch.match required")
    if "caseSensitive" in data:
        out["case_sensitive"] = data["caseSensitive"]
    return out
