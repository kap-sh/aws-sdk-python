"""Generated from Smithy shape ``com.amazonaws.dataexchange#LFTag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dataexchange.types.list_of_lf_tag_values


class LFTag(TypedDict, closed=True):
    tag_key: "str"
    """<p>The key name for the LF-tag.</p>"""
    tag_values: "capo_dataexchange.types.list_of_lf_tag_values.ListOfLFTagValues"
    """<p>A list of LF-tag values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LFTag) -> dict:
    out: dict = {}
    out["TagKey"] = value["tag_key"]
    import capo_dataexchange.types.list_of_lf_tag_values

    out["TagValues"] = capo_dataexchange.types.list_of_lf_tag_values.serialize_json(
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
        import capo_dataexchange.types.list_of_lf_tag_values

        out["tag_values"] = (
            capo_dataexchange.types.list_of_lf_tag_values.deserialize_json(
                data["TagValues"]
            )
        )
    else:
        raise DeserializationError("LFTag.tag_values required")
    return out
