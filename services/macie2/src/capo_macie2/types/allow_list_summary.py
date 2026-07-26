"""Generated from Smithy shape ``com.amazonaws.macie2#AllowListSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__string_min1_max128_pattern
    import capo_macie2.types.__string_min1_max512_pattern_ss
    import capo_macie2.types.__string_min22_max22_pattern_az0922
    import capo_macie2.types.__string_min71_max89_pattern_arn_aws_aws_cn_aws_us_gov_macie2_az19920_d12_allow_list_az0922
    import capo_macie2.types.__timestamp_iso8601


class AllowListSummary(TypedDict, closed=True):
    arn: NotRequired[
        "capo_macie2.types.__string_min71_max89_pattern_arn_aws_aws_cn_aws_us_gov_macie2_az19920_d12_allow_list_az0922.__stringMin71Max89PatternArnAwsAwsCnAwsUsGovMacie2AZ19920D12AllowListAZ0922"
    ]
    """<p>The Amazon Resource Name (ARN) of the allow list.</p>"""
    created_at: NotRequired["capo_macie2.types.__timestamp_iso8601.__timestampIso8601"]
    """<p>The date and time, in UTC and extended ISO 8601 format, when the allow list was created in Amazon Macie.</p>"""
    description: NotRequired[
        "capo_macie2.types.__string_min1_max512_pattern_ss.__stringMin1Max512PatternSS"
    ]
    """<p>The custom description of the allow list.</p>"""
    id: NotRequired[
        "capo_macie2.types.__string_min22_max22_pattern_az0922.__stringMin22Max22PatternAZ0922"
    ]
    """<p>The unique identifier for the allow list.</p>"""
    name: NotRequired[
        "capo_macie2.types.__string_min1_max128_pattern.__stringMin1Max128Pattern"
    ]
    """<p>The custom name of the allow list.</p>"""
    updated_at: NotRequired["capo_macie2.types.__timestamp_iso8601.__timestampIso8601"]
    """<p>The date and time, in UTC and extended ISO 8601 format, when the allow list's settings were most recently changed in Amazon Macie.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AllowListSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "created_at" in value:
        import capo_macie2.types.__timestamp_iso8601

        out["createdAt"] = capo_macie2.types.__timestamp_iso8601.serialize_json(
            value["created_at"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "updated_at" in value:
        import capo_macie2.types.__timestamp_iso8601

        out["updatedAt"] = capo_macie2.types.__timestamp_iso8601.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> AllowListSummary:
    out: AllowListSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "createdAt" in data:
        import capo_macie2.types.__timestamp_iso8601

        out["created_at"] = capo_macie2.types.__timestamp_iso8601.deserialize_json(
            data["createdAt"]
        )
    if "description" in data:
        out["description"] = data["description"]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "updatedAt" in data:
        import capo_macie2.types.__timestamp_iso8601

        out["updated_at"] = capo_macie2.types.__timestamp_iso8601.deserialize_json(
            data["updatedAt"]
        )
    return out
