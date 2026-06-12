"""Generated from Smithy shape ``com.amazonaws.support#DescribeCasesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_support.types.after_time
    import aws_sdk_support.types.before_time
    import aws_sdk_support.types.case_id_list
    import aws_sdk_support.types.display_id
    import aws_sdk_support.types.include_communications
    import aws_sdk_support.types.include_resolved_cases
    import aws_sdk_support.types.language
    import aws_sdk_support.types.max_results
    import aws_sdk_support.types.next_token


class DescribeCasesRequest(TypedDict):
    case_id_list: NotRequired["aws_sdk_support.types.case_id_list.CaseIdList"]
    """<p>A list of ID numbers of the support cases you want returned. The maximum number of cases is 100.</p>"""
    display_id: NotRequired["aws_sdk_support.types.display_id.DisplayId"]
    """<p>The ID displayed for a case in the Amazon Web Services Support Center user interface.</p>"""
    after_time: NotRequired["aws_sdk_support.types.after_time.AfterTime"]
    """<p>The start date for a filtered date search on support case communications. Case communications are available for 12 months after creation.</p>"""
    before_time: NotRequired["aws_sdk_support.types.before_time.BeforeTime"]
    """<p>The end date for a filtered date search on support case communications. Case communications are available for 12 months after creation.</p>"""
    include_resolved_cases: (
        "aws_sdk_support.types.include_resolved_cases.IncludeResolvedCases"
    )
    """<p>Specifies whether to include resolved support cases in the <code>DescribeCases</code> response. By default, resolved cases aren't included.</p>"""
    next_token: NotRequired["aws_sdk_support.types.next_token.NextToken"]
    """<p>A resumption point for pagination.</p>"""
    max_results: NotRequired["aws_sdk_support.types.max_results.MaxResults"]
    """<p>The maximum number of results to return before paginating.</p>"""
    language: NotRequired["aws_sdk_support.types.language.Language"]
    """<p>The language in which Amazon Web Services Support handles the case. Amazon Web Services Support currently supports Chinese (“zh”), English (\"en\"), Japanese (\"ja\") and Korean (“ko”). You must specify the ISO 639-1 code for the <code>language</code> parameter if you want support in that language.</p>"""
    include_communications: NotRequired[
        "aws_sdk_support.types.include_communications.IncludeCommunications"
    ]
    """<p>Specifies whether to include communications in the <code>DescribeCases</code> response. By default, communications are included.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCasesRequest) -> dict:
    out: dict = {}
    if "case_id_list" in value:
        import aws_sdk_support.types.case_id_list

        out["caseIdList"] = aws_sdk_support.types.case_id_list.serialize_aws_json_1_1(
            value["case_id_list"]
        )
    if "display_id" in value:
        out["displayId"] = value["display_id"]
    if "after_time" in value:
        out["afterTime"] = value["after_time"]
    if "before_time" in value:
        out["beforeTime"] = value["before_time"]
    out["includeResolvedCases"] = value.get("include_resolved_cases", False)
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "language" in value:
        out["language"] = value["language"]
    if "include_communications" in value:
        out["includeCommunications"] = value["include_communications"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCasesRequest:
    out: DescribeCasesRequest = {}  # type: ignore[typeddict-item]
    if "caseIdList" in data:
        import aws_sdk_support.types.case_id_list

        out["case_id_list"] = (
            aws_sdk_support.types.case_id_list.deserialize_aws_json_1_1(
                data["caseIdList"]
            )
        )
    if "displayId" in data:
        out["display_id"] = data["displayId"]
    if "afterTime" in data:
        out["after_time"] = data["afterTime"]
    if "beforeTime" in data:
        out["before_time"] = data["beforeTime"]
    if "includeResolvedCases" in data:
        out["include_resolved_cases"] = data["includeResolvedCases"]
    else:
        out["include_resolved_cases"] = False
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "language" in data:
        out["language"] = data["language"]
    if "includeCommunications" in data:
        out["include_communications"] = data["includeCommunications"]
    return out
