"""Generated from Smithy shape ``com.amazonaws.securityhub#CreateInsightRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_security_finding_filters
    import aws_sdk_securityhub.types.non_empty_string


class CreateInsightRequest(TypedDict):
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the custom insight to create.</p>"""
    filters: NotRequired[
        "aws_sdk_securityhub.types.aws_security_finding_filters.AwsSecurityFindingFilters"
    ]
    """<p>One or more attributes used to filter the findings included in the insight. The insight only includes findings that match the criteria defined in the filters.</p>"""
    group_by_attribute: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The attribute used to group the findings for the insight. The grouping attribute identifies the type of item that the insight applies to. For example, if an insight is grouped by resource identifier, then the insight produces a list of resource identifiers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateInsightRequest) -> dict:
    out: dict = {}
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


def deserialize_json(data: dict) -> CreateInsightRequest:
    out: CreateInsightRequest = {}  # type: ignore[typeddict-item]
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
