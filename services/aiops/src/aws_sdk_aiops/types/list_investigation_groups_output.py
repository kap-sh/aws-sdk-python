"""Generated from Smithy shape ``com.amazonaws.aiops#ListInvestigationGroupsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_aiops.types.investigation_groups
    import aws_sdk_aiops.types.sensitive_string_with_length_limits


class ListInvestigationGroupsOutput(TypedDict):
    next_token: NotRequired[
        "aws_sdk_aiops.types.sensitive_string_with_length_limits.SensitiveStringWithLengthLimits"
    ]
    """<p>Include this value in your next use of this operation to get the next set of service operations.</p>"""
    investigation_groups: NotRequired[
        "aws_sdk_aiops.types.investigation_groups.InvestigationGroups"
    ]
    """<p>An array of structures, where each structure contains the information about one investigation group in the account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInvestigationGroupsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "investigation_groups" in value:
        import aws_sdk_aiops.types.investigation_groups

        out["investigationGroups"] = (
            aws_sdk_aiops.types.investigation_groups.serialize_json(
                value["investigation_groups"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListInvestigationGroupsOutput:
    out: ListInvestigationGroupsOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "investigationGroups" in data:
        import aws_sdk_aiops.types.investigation_groups

        out["investigation_groups"] = (
            aws_sdk_aiops.types.investigation_groups.deserialize_json(
                data["investigationGroups"]
            )
        )
    return out
