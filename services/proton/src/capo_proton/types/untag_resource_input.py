"""Generated from Smithy shape ``com.amazonaws.proton#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.arn
    import capo_proton.types.tag_key_list


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_proton.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource to remove customer tags from.</p>"""
    tag_keys: "capo_proton.types.tag_key_list.TagKeyList"
    """<p>A list of customer tag keys that indicate the customer tags to be removed from the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceInput) -> dict:
    out: dict = {}
    import capo_proton.types.tag_key_list

    out["tagKeys"] = capo_proton.types.tag_key_list.serialize_aws_json_1_0(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    if "tagKeys" in data:
        import capo_proton.types.tag_key_list

        out["tag_keys"] = capo_proton.types.tag_key_list.deserialize_aws_json_1_0(
            data["tagKeys"]
        )
    else:
        raise DeserializationError("UntagResourceInput.tag_keys required")
    return out
