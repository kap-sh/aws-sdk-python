"""Generated from Smithy shape ``com.amazonaws.macie2#CreateCustomDataIdentifierRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__integer
    import aws_sdk_macie2.types.__list_of__string
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.severity_level_list
    import aws_sdk_macie2.types.tag_map


class CreateCustomDataIdentifierRequest(TypedDict, closed=True):
    client_token: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>A unique, case-sensitive token that you provide to ensure the idempotency of the request.</p>"""
    description: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>A custom description of the custom data identifier. The description can contain as many as 512 characters.</p> <p>We strongly recommend that you avoid including any sensitive data in the description of a custom data identifier. Other users of your account might be able to see this description, depending on the actions that they're allowed to perform in Amazon Macie.</p>"""
    ignore_words: NotRequired["aws_sdk_macie2.types.__list_of__string.__listOf__string"]
    """<p>An array that lists specific character sequences (<i>ignore words</i>) to exclude from the results. If the text matched by the regular expression contains any string in this array, Amazon Macie ignores it. The array can contain as many as 10 ignore words. Each ignore word can contain 4-90 UTF-8 characters. Ignore words are case sensitive.</p>"""
    keywords: NotRequired["aws_sdk_macie2.types.__list_of__string.__listOf__string"]
    """<p>An array that lists specific character sequences (<i>keywords</i>), one of which must precede and be within proximity (maximumMatchDistance) of the regular expression to match. The array can contain as many as 50 keywords. Each keyword can contain 3-90 UTF-8 characters. Keywords aren't case sensitive.</p>"""
    maximum_match_distance: NotRequired["aws_sdk_macie2.types.__integer.__integer"]
    """<p>The maximum number of characters that can exist between the end of at least one complete character sequence specified by the keywords array and the end of the text that matches the regex pattern. If a complete keyword precedes all the text that matches the pattern and the keyword is within the specified distance, Amazon Macie includes the result. The distance can be 1-300 characters. The default value is 50.</p>"""
    name: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>A custom name for the custom data identifier. The name can contain as many as 128 characters.</p> <p>We strongly recommend that you avoid including any sensitive data in the name of a custom data identifier. Other users of your account might be able to see this name, depending on the actions that they're allowed to perform in Amazon Macie.</p>"""
    regex: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The regular expression (<i>regex</i>) that defines the pattern to match. The expression can contain as many as 512 characters.</p>"""
    severity_levels: NotRequired[
        "aws_sdk_macie2.types.severity_level_list.SeverityLevelList"
    ]
    """<p>The severity to assign to findings that the custom data identifier produces, based on the number of occurrences of text that match the custom data identifier's detection criteria. You can specify as many as three SeverityLevel objects in this array, one for each severity: LOW, MEDIUM, or HIGH. If you specify more than one, the occurrences thresholds must be in ascending order by severity, moving from LOW to HIGH. For example, 1 for LOW, 50 for MEDIUM, and 100 for HIGH. If an S3 object contains fewer occurrences than the lowest specified threshold, Amazon Macie doesn't create a finding.</p> <p>If you don't specify any values for this array, Macie creates findings for S3 objects that contain at least one occurrence of text that matches the detection criteria, and Macie assigns the MEDIUM severity to those findings.</p>"""
    tags: NotRequired["aws_sdk_macie2.types.tag_map.TagMap"]
    """<p>A map of key-value pairs that specifies the tags to associate with the custom data identifier.</p> <p>A custom data identifier can have a maximum of 50 tags. Each tag consists of a tag key and an associated tag value. The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCustomDataIdentifierRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "description" in value:
        out["description"] = value["description"]
    if "ignore_words" in value:
        import aws_sdk_macie2.types.__list_of__string

        out["ignoreWords"] = aws_sdk_macie2.types.__list_of__string.serialize_json(
            value["ignore_words"]
        )
    if "keywords" in value:
        import aws_sdk_macie2.types.__list_of__string

        out["keywords"] = aws_sdk_macie2.types.__list_of__string.serialize_json(
            value["keywords"]
        )
    if "maximum_match_distance" in value:
        out["maximumMatchDistance"] = value["maximum_match_distance"]
    if "name" in value:
        out["name"] = value["name"]
    if "regex" in value:
        out["regex"] = value["regex"]
    if "severity_levels" in value:
        import aws_sdk_macie2.types.severity_level_list

        out["severityLevels"] = aws_sdk_macie2.types.severity_level_list.serialize_json(
            value["severity_levels"]
        )
    if "tags" in value:
        import aws_sdk_macie2.types.tag_map

        out["tags"] = aws_sdk_macie2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateCustomDataIdentifierRequest:
    out: CreateCustomDataIdentifierRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "description" in data:
        out["description"] = data["description"]
    if "ignoreWords" in data:
        import aws_sdk_macie2.types.__list_of__string

        out["ignore_words"] = aws_sdk_macie2.types.__list_of__string.deserialize_json(
            data["ignoreWords"]
        )
    if "keywords" in data:
        import aws_sdk_macie2.types.__list_of__string

        out["keywords"] = aws_sdk_macie2.types.__list_of__string.deserialize_json(
            data["keywords"]
        )
    if "maximumMatchDistance" in data:
        out["maximum_match_distance"] = data["maximumMatchDistance"]
    if "name" in data:
        out["name"] = data["name"]
    if "regex" in data:
        out["regex"] = data["regex"]
    if "severityLevels" in data:
        import aws_sdk_macie2.types.severity_level_list

        out["severity_levels"] = (
            aws_sdk_macie2.types.severity_level_list.deserialize_json(
                data["severityLevels"]
            )
        )
    if "tags" in data:
        import aws_sdk_macie2.types.tag_map

        out["tags"] = aws_sdk_macie2.types.tag_map.deserialize_json(data["tags"])
    return out
