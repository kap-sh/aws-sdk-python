"""Generated from Smithy shape ``com.amazonaws.rbin#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_rbin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rbin.types.rule_arn
    import capo_rbin.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_rbin.types.rule_arn.RuleArn"
    """<p>The Amazon Resource Name (ARN) of the retention rule.</p>"""
    tags: "capo_rbin.types.tag_list.TagList"
    """<p>Information about the tags to assign to the retention rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_rbin.types.tag_list

    out["Tags"] = capo_rbin.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_rbin.types.tag_list

        out["tags"] = capo_rbin.types.tag_list.deserialize_json(data["Tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
