"""Generated from Smithy shape ``com.amazonaws.securityhub#UpdateInsightRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_security_finding_filters
    import capo_securityhub.types.non_empty_string


class UpdateInsightRequest(TypedDict, closed=True):
    insight_arn: "capo_securityhub.types.non_empty_string.NonEmptyString"
    """<p>The ARN of the insight that you want to update.</p>"""
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The updated name for the insight.</p>"""
    filters: NotRequired[
        "capo_securityhub.types.aws_security_finding_filters.AwsSecurityFindingFilters"
    ]
    """<p>The updated filters that define this insight.</p>"""
    group_by_attribute: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The updated <code>GroupBy</code> attribute that defines this insight.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateInsightRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "filters" in value:
        import capo_securityhub.types.aws_security_finding_filters

        out["Filters"] = (
            capo_securityhub.types.aws_security_finding_filters.serialize_json(
                value["filters"]
            )
        )
    if "group_by_attribute" in value:
        out["GroupByAttribute"] = value["group_by_attribute"]
    return out


def deserialize_json(data: dict) -> UpdateInsightRequest:
    out: UpdateInsightRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Filters" in data:
        import capo_securityhub.types.aws_security_finding_filters

        out["filters"] = (
            capo_securityhub.types.aws_security_finding_filters.deserialize_json(
                data["Filters"]
            )
        )
    if "GroupByAttribute" in data:
        out["group_by_attribute"] = data["GroupByAttribute"]
    return out
