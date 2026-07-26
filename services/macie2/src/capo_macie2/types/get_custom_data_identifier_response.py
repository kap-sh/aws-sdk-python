"""Generated from Smithy shape ``com.amazonaws.macie2#GetCustomDataIdentifierResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__boolean
    import capo_macie2.types.__integer
    import capo_macie2.types.__list_of__string
    import capo_macie2.types.__string
    import capo_macie2.types.__timestamp_iso8601
    import capo_macie2.types.severity_level_list
    import capo_macie2.types.tag_map


class GetCustomDataIdentifierResponse(TypedDict, closed=True):
    arn: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the custom data identifier.</p>"""
    created_at: NotRequired["capo_macie2.types.__timestamp_iso8601.__timestampIso8601"]
    """<p>The date and time, in UTC and extended ISO 8601 format, when the custom data identifier was created.</p>"""
    deleted: NotRequired["capo_macie2.types.__boolean.__boolean"]
    """<p>Specifies whether the custom data identifier was deleted. If you delete a custom data identifier, Amazon Macie doesn't delete it permanently. Instead, it soft deletes the identifier.</p>"""
    description: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The custom description of the custom data identifier.</p>"""
    id: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The unique identifier for the custom data identifier.</p>"""
    ignore_words: NotRequired["capo_macie2.types.__list_of__string.__listOf__string"]
    """<p>An array that lists specific character sequences (<i>ignore words</i>) to exclude from the results. If the text matched by the regular expression contains any string in this array, Amazon Macie ignores it. Ignore words are case sensitive.</p>"""
    keywords: NotRequired["capo_macie2.types.__list_of__string.__listOf__string"]
    """<p>An array that lists specific character sequences (<i>keywords</i>), one of which must precede and be within proximity (maximumMatchDistance) of the regular expression to match. Keywords aren't case sensitive.</p>"""
    maximum_match_distance: NotRequired["capo_macie2.types.__integer.__integer"]
    """<p>The maximum number of characters that can exist between the end of at least one complete character sequence specified by the keywords array and the end of the text that matches the regex pattern. If a complete keyword precedes all the text that matches the pattern and the keyword is within the specified distance, Amazon Macie includes the result. Otherwise, Macie excludes the result.</p>"""
    name: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The custom name of the custom data identifier.</p>"""
    regex: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The regular expression (<i>regex</i>) that defines the pattern to match.</p>"""
    severity_levels: NotRequired[
        "capo_macie2.types.severity_level_list.SeverityLevelList"
    ]
    """<p>Specifies the severity that's assigned to findings that the custom data identifier produces, based on the number of occurrences of text that match the custom data identifier's detection criteria. By default, Amazon Macie creates findings for S3 objects that contain at least one occurrence of text that matches the detection criteria, and Macie assigns the MEDIUM severity to those findings.</p>"""
    tags: NotRequired["capo_macie2.types.tag_map.TagMap"]
    """<p>A map of key-value pairs that identifies the tags (keys and values) that are associated with the custom data identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCustomDataIdentifierResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "created_at" in value:
        import capo_macie2.types.__timestamp_iso8601

        out["createdAt"] = capo_macie2.types.__timestamp_iso8601.serialize_json(
            value["created_at"]
        )
    if "deleted" in value:
        out["deleted"] = value["deleted"]
    if "description" in value:
        out["description"] = value["description"]
    if "id" in value:
        out["id"] = value["id"]
    if "ignore_words" in value:
        import capo_macie2.types.__list_of__string

        out["ignoreWords"] = capo_macie2.types.__list_of__string.serialize_json(
            value["ignore_words"]
        )
    if "keywords" in value:
        import capo_macie2.types.__list_of__string

        out["keywords"] = capo_macie2.types.__list_of__string.serialize_json(
            value["keywords"]
        )
    if "maximum_match_distance" in value:
        out["maximumMatchDistance"] = value["maximum_match_distance"]
    if "name" in value:
        out["name"] = value["name"]
    if "regex" in value:
        out["regex"] = value["regex"]
    if "severity_levels" in value:
        import capo_macie2.types.severity_level_list

        out["severityLevels"] = capo_macie2.types.severity_level_list.serialize_json(
            value["severity_levels"]
        )
    if "tags" in value:
        import capo_macie2.types.tag_map

        out["tags"] = capo_macie2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetCustomDataIdentifierResponse:
    out: GetCustomDataIdentifierResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "createdAt" in data:
        import capo_macie2.types.__timestamp_iso8601

        out["created_at"] = capo_macie2.types.__timestamp_iso8601.deserialize_json(
            data["createdAt"]
        )
    if "deleted" in data:
        out["deleted"] = data["deleted"]
    if "description" in data:
        out["description"] = data["description"]
    if "id" in data:
        out["id"] = data["id"]
    if "ignoreWords" in data:
        import capo_macie2.types.__list_of__string

        out["ignore_words"] = capo_macie2.types.__list_of__string.deserialize_json(
            data["ignoreWords"]
        )
    if "keywords" in data:
        import capo_macie2.types.__list_of__string

        out["keywords"] = capo_macie2.types.__list_of__string.deserialize_json(
            data["keywords"]
        )
    if "maximumMatchDistance" in data:
        out["maximum_match_distance"] = data["maximumMatchDistance"]
    if "name" in data:
        out["name"] = data["name"]
    if "regex" in data:
        out["regex"] = data["regex"]
    if "severityLevels" in data:
        import capo_macie2.types.severity_level_list

        out["severity_levels"] = capo_macie2.types.severity_level_list.deserialize_json(
            data["severityLevels"]
        )
    if "tags" in data:
        import capo_macie2.types.tag_map

        out["tags"] = capo_macie2.types.tag_map.deserialize_json(data["tags"])
    return out
