"""Generated from Smithy shape ``com.amazonaws.proton#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.arn
    import capo_proton.types.tag_list


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_proton.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Proton resource to apply customer tags to.</p>"""
    tags: "capo_proton.types.tag_list.TagList"
    """<p>A list of customer tags to apply to the Proton resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceInput) -> dict:
    out: dict = {}
    import capo_proton.types.tag_list

    out["tags"] = capo_proton.types.tag_list.serialize_aws_json_1_0(value["tags"])
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_proton.types.tag_list

        out["tags"] = capo_proton.types.tag_list.deserialize_aws_json_1_0(data["tags"])
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out
