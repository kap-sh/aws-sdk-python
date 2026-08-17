"""Generated from Smithy shape ``com.amazonaws.lambda#PropagateTags``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.propagate_tags_mode
    import capo_lambda.types.tags


class PropagateTags(TypedDict, closed=True):
    mode: NotRequired["capo_lambda.types.propagate_tags_mode.PropagateTagsMode"]
    """<p>The tag propagation mode. Set to <code>Explicit</code> to propagate the tags specified in <code>ExplicitTags</code> to managed resources. Set to <code>None</code> to disable tag propagation.</p>"""
    explicit_tags: NotRequired["capo_lambda.types.tags.Tags"]
    """<p>A list of tags to apply to managed resources when <code>Mode</code> is set to <code>Explicit</code>. You can specify up to 40 tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PropagateTags) -> dict:
    out: dict = {}
    if "mode" in value:
        import capo_lambda.types.propagate_tags_mode

        out["Mode"] = capo_lambda.types.propagate_tags_mode.serialize_json(
            value["mode"]
        )
    if "explicit_tags" in value:
        import capo_lambda.types.tags

        out["ExplicitTags"] = capo_lambda.types.tags.serialize_json(
            value["explicit_tags"]
        )
    return out


def deserialize_json(data: dict) -> PropagateTags:
    out: PropagateTags = {}  # type: ignore[typeddict-item]
    if data.get("Mode") is not None:
        import capo_lambda.types.propagate_tags_mode

        out["mode"] = capo_lambda.types.propagate_tags_mode.deserialize_json(
            data["Mode"]
        )
    if data.get("ExplicitTags") is not None:
        import capo_lambda.types.tags

        out["explicit_tags"] = capo_lambda.types.tags.deserialize_json(
            data["ExplicitTags"]
        )
    return out
