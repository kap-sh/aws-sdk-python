"""Generated from Smithy shape ``com.amazonaws.ssmsap#ListApplicationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.application_summary_list
    import aws_sdk_ssm_sap.types.next_token


class ListApplicationsOutput(TypedDict, closed=True):
    applications: NotRequired[
        "aws_sdk_ssm_sap.types.application_summary_list.ApplicationSummaryList"
    ]
    """<p>The applications registered with AWS Systems Manager for SAP.</p>"""
    next_token: NotRequired["aws_sdk_ssm_sap.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationsOutput) -> dict:
    out: dict = {}
    if "applications" in value:
        import aws_sdk_ssm_sap.types.application_summary_list

        out["Applications"] = (
            aws_sdk_ssm_sap.types.application_summary_list.serialize_json(
                value["applications"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListApplicationsOutput:
    out: ListApplicationsOutput = {}  # type: ignore[typeddict-item]
    if "Applications" in data:
        import aws_sdk_ssm_sap.types.application_summary_list

        out["applications"] = (
            aws_sdk_ssm_sap.types.application_summary_list.deserialize_json(
                data["Applications"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
