"""Generated from Smithy shape ``com.amazonaws.lakeformation#LFTag``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.lf_tag_key
    import aws_sdk_lakeformation.types.tag_value_list


class LFTag(TypedDict):
    tag_key: "aws_sdk_lakeformation.types.lf_tag_key.LFTagKey"
    """<p>The key-name for the LF-tag.</p>"""
    tag_values: "aws_sdk_lakeformation.types.tag_value_list.TagValueList"
    """<p>A list of possible values an attribute can take.</p> <p>The maximum number of values that can be defined for a LF-Tag is 1000. A single API call supports 50 values. You can use multiple API calls to add more values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LFTag) -> dict:
    out: dict = {}
    out["TagKey"] = value["tag_key"]
    import aws_sdk_lakeformation.types.tag_value_list

    out["TagValues"] = aws_sdk_lakeformation.types.tag_value_list.serialize_json(
        value["tag_values"]
    )
    return out


def deserialize_json(data: dict) -> LFTag:
    out: LFTag = {}  # type: ignore[typeddict-item]
    if "TagKey" in data:
        out["tag_key"] = data["TagKey"]
    else:
        raise DeserializationError("LFTag.tag_key required")
    if "TagValues" in data:
        import aws_sdk_lakeformation.types.tag_value_list

        out["tag_values"] = aws_sdk_lakeformation.types.tag_value_list.deserialize_json(
            data["TagValues"]
        )
    else:
        raise DeserializationError("LFTag.tag_values required")
    return out
