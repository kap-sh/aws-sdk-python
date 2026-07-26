"""Generated from Smithy shape ``com.amazonaws.vpclattice#HttpMatch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.header_match_list
    import capo_vpc_lattice.types.http_method
    import capo_vpc_lattice.types.path_match


class HttpMatch(TypedDict, closed=True):
    method: NotRequired["capo_vpc_lattice.types.http_method.HttpMethod"]
    """<p>The HTTP method type.</p>"""
    path_match: NotRequired["capo_vpc_lattice.types.path_match.PathMatch"]
    """<p>The path match.</p>"""
    header_matches: NotRequired[
        "capo_vpc_lattice.types.header_match_list.HeaderMatchList"
    ]
    """<p>The header matches. Matches incoming requests with rule based on request header value before applying rule action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpMatch) -> dict:
    out: dict = {}
    if "method" in value:
        out["method"] = value["method"]
    if "path_match" in value:
        import capo_vpc_lattice.types.path_match

        out["pathMatch"] = capo_vpc_lattice.types.path_match.serialize_json(
            value["path_match"]
        )
    if "header_matches" in value:
        import capo_vpc_lattice.types.header_match_list

        out["headerMatches"] = capo_vpc_lattice.types.header_match_list.serialize_json(
            value["header_matches"]
        )
    return out


def deserialize_json(data: dict) -> HttpMatch:
    out: HttpMatch = {}  # type: ignore[typeddict-item]
    if "method" in data:
        out["method"] = data["method"]
    if "pathMatch" in data:
        import capo_vpc_lattice.types.path_match

        out["path_match"] = capo_vpc_lattice.types.path_match.deserialize_json(
            data["pathMatch"]
        )
    if "headerMatches" in data:
        import capo_vpc_lattice.types.header_match_list

        out["header_matches"] = (
            capo_vpc_lattice.types.header_match_list.deserialize_json(
                data["headerMatches"]
            )
        )
    return out
