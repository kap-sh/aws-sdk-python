"""Generated from Smithy shape ``com.amazonaws.dataexchange#CreateRevisionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.__string_min0_max16384
    import capo_dataexchange.types.id
    import capo_dataexchange.types.map_of__string


class CreateRevisionRequest(TypedDict, closed=True):
    comment: NotRequired[
        "capo_dataexchange.types.__string_min0_max16384.__stringMin0Max16384"
    ]
    """<p>An optional comment about the revision.</p>"""
    data_set_id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for a data set.</p>"""
    tags: NotRequired["capo_dataexchange.types.map_of__string.MapOf__string"]
    """<p>A revision tag is an optional label that you can assign to a revision when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to these data sets and revisions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRevisionRequest) -> dict:
    out: dict = {}
    if "comment" in value:
        out["Comment"] = value["comment"]
    if "tags" in value:
        import capo_dataexchange.types.map_of__string

        out["Tags"] = capo_dataexchange.types.map_of__string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateRevisionRequest:
    out: CreateRevisionRequest = {}  # type: ignore[typeddict-item]
    if "Comment" in data:
        out["comment"] = data["Comment"]
    if "Tags" in data:
        import capo_dataexchange.types.map_of__string

        out["tags"] = capo_dataexchange.types.map_of__string.deserialize_json(
            data["Tags"]
        )
    return out
