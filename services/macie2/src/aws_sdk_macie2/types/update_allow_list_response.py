"""Generated from Smithy shape ``com.amazonaws.macie2#UpdateAllowListResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string_min22_max22_pattern_az0922
    import aws_sdk_macie2.types.__string_min71_max89_pattern_arn_aws_aws_cn_aws_us_gov_macie2_az19920_d12_allow_list_az0922


class UpdateAllowListResponse(TypedDict):
    arn: NotRequired[
        "aws_sdk_macie2.types.__string_min71_max89_pattern_arn_aws_aws_cn_aws_us_gov_macie2_az19920_d12_allow_list_az0922.__stringMin71Max89PatternArnAwsAwsCnAwsUsGovMacie2AZ19920D12AllowListAZ0922"
    ]
    """<p>The Amazon Resource Name (ARN) of the allow list.</p>"""
    id: NotRequired[
        "aws_sdk_macie2.types.__string_min22_max22_pattern_az0922.__stringMin22Max22PatternAZ0922"
    ]
    """<p>The unique identifier for the allow list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAllowListResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> UpdateAllowListResponse:
    out: UpdateAllowListResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "id" in data:
        out["id"] = data["id"]
    return out
