"""Generated from Smithy shape ``com.amazonaws.inspector2#CodeRepositoryAggregationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.severity_counts


class CodeRepositoryAggregationResponse(TypedDict, closed=True):
    project_names: "str"
    """<p>The names of the projects associated with the code repository.</p>"""
    provider_type: NotRequired["str"]
    """<p>The type of repository provider for the code repository.</p>"""
    severity_counts: NotRequired[
        "aws_sdk_inspector2.types.severity_counts.SeverityCounts"
    ]
    exploit_available_active_findings_count: NotRequired["int"]
    """<p>The number of active findings that have an exploit available for the code repository.</p>"""
    fix_available_active_findings_count: NotRequired["int"]
    """<p>The number of active findings that have a fix available for the code repository.</p>"""
    account_id: NotRequired["str"]
    """<p>The Amazon Web Services account ID associated with the code repository.</p>"""
    resource_id: NotRequired["str"]
    """<p>The resource ID of the code repository.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeRepositoryAggregationResponse) -> dict:
    out: dict = {}
    out["projectNames"] = value["project_names"]
    if "provider_type" in value:
        out["providerType"] = value["provider_type"]
    if "severity_counts" in value:
        import aws_sdk_inspector2.types.severity_counts

        out["severityCounts"] = aws_sdk_inspector2.types.severity_counts.serialize_json(
            value["severity_counts"]
        )
    if "exploit_available_active_findings_count" in value:
        out["exploitAvailableActiveFindingsCount"] = value[
            "exploit_available_active_findings_count"
        ]
    if "fix_available_active_findings_count" in value:
        out["fixAvailableActiveFindingsCount"] = value[
            "fix_available_active_findings_count"
        ]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    return out


def deserialize_json(data: dict) -> CodeRepositoryAggregationResponse:
    out: CodeRepositoryAggregationResponse = {}  # type: ignore[typeddict-item]
    if "projectNames" in data:
        out["project_names"] = data["projectNames"]
    else:
        raise DeserializationError(
            "CodeRepositoryAggregationResponse.project_names required"
        )
    if "providerType" in data:
        out["provider_type"] = data["providerType"]
    if "severityCounts" in data:
        import aws_sdk_inspector2.types.severity_counts

        out["severity_counts"] = (
            aws_sdk_inspector2.types.severity_counts.deserialize_json(
                data["severityCounts"]
            )
        )
    if "exploitAvailableActiveFindingsCount" in data:
        out["exploit_available_active_findings_count"] = data[
            "exploitAvailableActiveFindingsCount"
        ]
    if "fixAvailableActiveFindingsCount" in data:
        out["fix_available_active_findings_count"] = data[
            "fixAvailableActiveFindingsCount"
        ]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    return out
