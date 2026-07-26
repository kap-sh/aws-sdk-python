"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#PathFormat``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.object_prefixes


class PathFormat(TypedDict, closed=True):
    object_prefixes: NotRequired[
        "capo_lex_models_v2.types.object_prefixes.ObjectPrefixes"
    ]
    """<p>A list of Amazon S3 prefixes that points to sub-folders in the Amazon S3 bucket. Specify this list if you only want Lex to read the files under this set of sub-folders.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PathFormat) -> dict:
    out: dict = {}
    if "object_prefixes" in value:
        import capo_lex_models_v2.types.object_prefixes

        out["objectPrefixes"] = capo_lex_models_v2.types.object_prefixes.serialize_json(
            value["object_prefixes"]
        )
    return out


def deserialize_json(data: dict) -> PathFormat:
    out: PathFormat = {}  # type: ignore[typeddict-item]
    if "objectPrefixes" in data:
        import capo_lex_models_v2.types.object_prefixes

        out["object_prefixes"] = (
            capo_lex_models_v2.types.object_prefixes.deserialize_json(
                data["objectPrefixes"]
            )
        )
    return out
