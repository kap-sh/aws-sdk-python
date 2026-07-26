"""Generated from Smithy shape ``com.amazonaws.macie2#JobScopeTerm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.simple_scope_term
    import capo_macie2.types.tag_scope_term


class JobScopeTerm(TypedDict, closed=True):
    simple_scope_term: NotRequired[
        "capo_macie2.types.simple_scope_term.SimpleScopeTerm"
    ]
    """<p>A property-based condition that defines a property, operator, and one or more values for including or excluding objects from the job.</p>"""
    tag_scope_term: NotRequired["capo_macie2.types.tag_scope_term.TagScopeTerm"]
    """<p>A tag-based condition that defines the operator and tag keys or tag key and value pairs for including or excluding objects from the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobScopeTerm) -> dict:
    out: dict = {}
    if "simple_scope_term" in value:
        import capo_macie2.types.simple_scope_term

        out["simpleScopeTerm"] = capo_macie2.types.simple_scope_term.serialize_json(
            value["simple_scope_term"]
        )
    if "tag_scope_term" in value:
        import capo_macie2.types.tag_scope_term

        out["tagScopeTerm"] = capo_macie2.types.tag_scope_term.serialize_json(
            value["tag_scope_term"]
        )
    return out


def deserialize_json(data: dict) -> JobScopeTerm:
    out: JobScopeTerm = {}  # type: ignore[typeddict-item]
    if "simpleScopeTerm" in data:
        import capo_macie2.types.simple_scope_term

        out["simple_scope_term"] = capo_macie2.types.simple_scope_term.deserialize_json(
            data["simpleScopeTerm"]
        )
    if "tagScopeTerm" in data:
        import capo_macie2.types.tag_scope_term

        out["tag_scope_term"] = capo_macie2.types.tag_scope_term.deserialize_json(
            data["tagScopeTerm"]
        )
    return out
