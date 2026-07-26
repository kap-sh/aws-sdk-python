"""Generated from Smithy shape ``com.amazonaws.macie2#CreateAllowListRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__string
    import capo_macie2.types.__string_min1_max128_pattern
    import capo_macie2.types.__string_min1_max512_pattern_ss
    import capo_macie2.types.allow_list_criteria
    import capo_macie2.types.tag_map


class CreateAllowListRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_macie2.types.__string.__string"]
    """<p>A unique, case-sensitive token that you provide to ensure the idempotency of the request.</p>"""
    criteria: NotRequired["capo_macie2.types.allow_list_criteria.AllowListCriteria"]
    """<p>The criteria that specify the text or text pattern to ignore. The criteria can be the location and name of an S3 object that lists specific text to ignore (s3WordsList), or a regular expression (regex) that defines a text pattern to ignore.</p>"""
    description: NotRequired[
        "capo_macie2.types.__string_min1_max512_pattern_ss.__stringMin1Max512PatternSS"
    ]
    """<p>A custom description of the allow list. The description can contain as many as 512 characters.</p>"""
    name: NotRequired[
        "capo_macie2.types.__string_min1_max128_pattern.__stringMin1Max128Pattern"
    ]
    """<p>A custom name for the allow list. The name can contain as many as 128 characters.</p>"""
    tags: NotRequired["capo_macie2.types.tag_map.TagMap"]
    """<p>A map of key-value pairs that specifies the tags to associate with the allow list.</p> <p>An allow list can have a maximum of 50 tags. Each tag consists of a tag key and an associated tag value. The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAllowListRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "criteria" in value:
        import capo_macie2.types.allow_list_criteria

        out["criteria"] = capo_macie2.types.allow_list_criteria.serialize_json(
            value["criteria"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "name" in value:
        out["name"] = value["name"]
    if "tags" in value:
        import capo_macie2.types.tag_map

        out["tags"] = capo_macie2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateAllowListRequest:
    out: CreateAllowListRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "criteria" in data:
        import capo_macie2.types.allow_list_criteria

        out["criteria"] = capo_macie2.types.allow_list_criteria.deserialize_json(
            data["criteria"]
        )
    if "description" in data:
        out["description"] = data["description"]
    if "name" in data:
        out["name"] = data["name"]
    if "tags" in data:
        import capo_macie2.types.tag_map

        out["tags"] = capo_macie2.types.tag_map.deserialize_json(data["tags"])
    return out
