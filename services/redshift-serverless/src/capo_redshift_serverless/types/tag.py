"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_redshift_serverless.types.tag_key
    import capo_redshift_serverless.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_redshift_serverless.types.tag_key.TagKey"
    """<p>The key to use in the tag.</p>"""
    value: "capo_redshift_serverless.types.tag_value.TagValue"
    """<p>The value of the tag.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tag) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("Tag.key required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("Tag.value required")
    return out
