"""Generated from Smithy shape ``com.amazonaws.appmesh#HttpPathMatch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.http_path_exact
    import aws_sdk_app_mesh.types.http_path_regex


class HttpPathMatch(TypedDict, closed=True):
    exact: NotRequired["aws_sdk_app_mesh.types.http_path_exact.HttpPathExact"]
    """<p>The exact path to match on.</p>"""
    regex: NotRequired["aws_sdk_app_mesh.types.http_path_regex.HttpPathRegex"]
    """<p>The regex used to match the path.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpPathMatch) -> dict:
    out: dict = {}
    if "exact" in value:
        out["exact"] = value["exact"]
    if "regex" in value:
        out["regex"] = value["regex"]
    return out


def deserialize_json(data: dict) -> HttpPathMatch:
    out: HttpPathMatch = {}  # type: ignore[typeddict-item]
    if "exact" in data:
        out["exact"] = data["exact"]
    if "regex" in data:
        out["regex"] = data["regex"]
    return out
