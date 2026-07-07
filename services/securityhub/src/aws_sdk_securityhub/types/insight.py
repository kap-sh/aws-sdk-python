"""Generated from Smithy shape ``com.amazonaws.securityhub#Insight``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_security_finding_filters
    import aws_sdk_securityhub.types.non_empty_string


class Insight(TypedDict, closed=True):
    insight_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of a Security Hub CSPM insight.</p>"""
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of a Security Hub CSPM insight.</p>"""
    filters: NotRequired[
        "aws_sdk_securityhub.types.aws_security_finding_filters.AwsSecurityFindingFilters"
    ]
    """<p>One or more attributes used to filter the findings included in the insight. You can filter by up to ten finding attributes. For each attribute, you can provide up to 20 filter values. The insight only includes findings that match the criteria defined in the filters.</p>"""
    group_by_attribute: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The grouping attribute for the insight's findings. Indicates how to group the matching findings, and identifies the type of item that the insight applies to. For example, if an insight is grouped by resource identifier, then the insight produces a list of resource identifiers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Insight) -> dict:
    out: dict = {}
    if "insight_arn" in value:
        out["InsightArn"] = value["insight_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "filters" in value:
        import aws_sdk_securityhub.types.aws_security_finding_filters

        out["Filters"] = (
            aws_sdk_securityhub.types.aws_security_finding_filters.serialize_json(
                value["filters"]
            )
        )
    if "group_by_attribute" in value:
        out["GroupByAttribute"] = value["group_by_attribute"]
    return out


def deserialize_json(data: dict) -> Insight:
    out: Insight = {}  # type: ignore[typeddict-item]
    if "InsightArn" in data:
        out["insight_arn"] = data["InsightArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Filters" in data:
        import aws_sdk_securityhub.types.aws_security_finding_filters

        out["filters"] = (
            aws_sdk_securityhub.types.aws_security_finding_filters.deserialize_json(
                data["Filters"]
            )
        )
    if "GroupByAttribute" in data:
        out["group_by_attribute"] = data["GroupByAttribute"]
    return out
