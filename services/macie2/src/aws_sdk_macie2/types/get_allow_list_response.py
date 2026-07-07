"""Generated from Smithy shape ``com.amazonaws.macie2#GetAllowListResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string_min1_max128_pattern
    import aws_sdk_macie2.types.__string_min1_max512_pattern_ss
    import aws_sdk_macie2.types.__string_min22_max22_pattern_az0922
    import aws_sdk_macie2.types.__string_min71_max89_pattern_arn_aws_aws_cn_aws_us_gov_macie2_az19920_d12_allow_list_az0922
    import aws_sdk_macie2.types.__timestamp_iso8601
    import aws_sdk_macie2.types.allow_list_criteria
    import aws_sdk_macie2.types.allow_list_status
    import aws_sdk_macie2.types.tag_map


class GetAllowListResponse(TypedDict, closed=True):
    arn: NotRequired[
        "aws_sdk_macie2.types.__string_min71_max89_pattern_arn_aws_aws_cn_aws_us_gov_macie2_az19920_d12_allow_list_az0922.__stringMin71Max89PatternArnAwsAwsCnAwsUsGovMacie2AZ19920D12AllowListAZ0922"
    ]
    """<p>The Amazon Resource Name (ARN) of the allow list.</p>"""
    created_at: NotRequired[
        "aws_sdk_macie2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The date and time, in UTC and extended ISO 8601 format, when the allow list was created in Amazon Macie.</p>"""
    criteria: NotRequired["aws_sdk_macie2.types.allow_list_criteria.AllowListCriteria"]
    """<p>The criteria that specify the text or text pattern to ignore. The criteria can be the location and name of an S3 object that lists specific text to ignore (s3WordsList), or a regular expression (regex) that defines a text pattern to ignore.</p>"""
    description: NotRequired[
        "aws_sdk_macie2.types.__string_min1_max512_pattern_ss.__stringMin1Max512PatternSS"
    ]
    """<p>The custom description of the allow list.</p>"""
    id: NotRequired[
        "aws_sdk_macie2.types.__string_min22_max22_pattern_az0922.__stringMin22Max22PatternAZ0922"
    ]
    """<p>The unique identifier for the allow list.</p>"""
    name: NotRequired[
        "aws_sdk_macie2.types.__string_min1_max128_pattern.__stringMin1Max128Pattern"
    ]
    """<p>The custom name of the allow list.</p>"""
    status: NotRequired["aws_sdk_macie2.types.allow_list_status.AllowListStatus"]
    """<p>The current status of the allow list, which indicates whether Amazon Macie can access and use the list's criteria.</p>"""
    tags: NotRequired["aws_sdk_macie2.types.tag_map.TagMap"]
    """<p>A map of key-value pairs that specifies which tags (keys and values) are associated with the allow list.</p>"""
    updated_at: NotRequired[
        "aws_sdk_macie2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The date and time, in UTC and extended ISO 8601 format, when the allow list's settings were most recently changed in Amazon Macie.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAllowListResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "created_at" in value:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["createdAt"] = aws_sdk_macie2.types.__timestamp_iso8601.serialize_json(
            value["created_at"]
        )
    if "criteria" in value:
        import aws_sdk_macie2.types.allow_list_criteria

        out["criteria"] = aws_sdk_macie2.types.allow_list_criteria.serialize_json(
            value["criteria"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        import aws_sdk_macie2.types.allow_list_status

        out["status"] = aws_sdk_macie2.types.allow_list_status.serialize_json(
            value["status"]
        )
    if "tags" in value:
        import aws_sdk_macie2.types.tag_map

        out["tags"] = aws_sdk_macie2.types.tag_map.serialize_json(value["tags"])
    if "updated_at" in value:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["updatedAt"] = aws_sdk_macie2.types.__timestamp_iso8601.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> GetAllowListResponse:
    out: GetAllowListResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "createdAt" in data:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["created_at"] = aws_sdk_macie2.types.__timestamp_iso8601.deserialize_json(
            data["createdAt"]
        )
    if "criteria" in data:
        import aws_sdk_macie2.types.allow_list_criteria

        out["criteria"] = aws_sdk_macie2.types.allow_list_criteria.deserialize_json(
            data["criteria"]
        )
    if "description" in data:
        out["description"] = data["description"]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "status" in data:
        import aws_sdk_macie2.types.allow_list_status

        out["status"] = aws_sdk_macie2.types.allow_list_status.deserialize_json(
            data["status"]
        )
    if "tags" in data:
        import aws_sdk_macie2.types.tag_map

        out["tags"] = aws_sdk_macie2.types.tag_map.deserialize_json(data["tags"])
    if "updatedAt" in data:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["updated_at"] = aws_sdk_macie2.types.__timestamp_iso8601.deserialize_json(
            data["updatedAt"]
        )
    return out
