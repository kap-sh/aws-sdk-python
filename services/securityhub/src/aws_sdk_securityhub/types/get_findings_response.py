"""Generated from Smithy shape ``com.amazonaws.securityhub#GetFindingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_security_finding_list
    import aws_sdk_securityhub.types.next_token


class GetFindingsResponse(TypedDict, closed=True):
    findings: NotRequired[
        "aws_sdk_securityhub.types.aws_security_finding_list.AwsSecurityFindingList"
    ]
    """<p>The findings that matched the filters specified in the request.</p>"""
    next_token: NotRequired["aws_sdk_securityhub.types.next_token.NextToken"]
    """<p>The pagination token to use to request the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingsResponse) -> dict:
    out: dict = {}
    if "findings" in value:
        import aws_sdk_securityhub.types.aws_security_finding_list

        out["Findings"] = (
            aws_sdk_securityhub.types.aws_security_finding_list.serialize_json(
                value["findings"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetFindingsResponse:
    out: GetFindingsResponse = {}  # type: ignore[typeddict-item]
    if "Findings" in data:
        import aws_sdk_securityhub.types.aws_security_finding_list

        out["findings"] = (
            aws_sdk_securityhub.types.aws_security_finding_list.deserialize_json(
                data["Findings"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
