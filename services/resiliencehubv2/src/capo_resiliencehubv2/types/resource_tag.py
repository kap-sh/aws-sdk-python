"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ResourceTag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.tag_key
    import capo_resiliencehubv2.types.tag_value_list


class ResourceTag(TypedDict, closed=True):
    key: "capo_resiliencehubv2.types.tag_key.TagKey"
    values: "capo_resiliencehubv2.types.tag_value_list.TagValueList"
    """<p>The list of tag values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceTag) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    import capo_resiliencehubv2.types.tag_value_list

    out["values"] = capo_resiliencehubv2.types.tag_value_list.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> ResourceTag:
    out: ResourceTag = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("ResourceTag.key required")
    if "values" in data:
        import capo_resiliencehubv2.types.tag_value_list

        out["values"] = capo_resiliencehubv2.types.tag_value_list.deserialize_json(
            data["values"]
        )
    else:
        raise DeserializationError("ResourceTag.values required")
    return out
