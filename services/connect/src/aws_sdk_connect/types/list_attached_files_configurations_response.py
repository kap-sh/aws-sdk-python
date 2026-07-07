"""Generated from Smithy shape ``com.amazonaws.connect#ListAttachedFilesConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.attached_files_configuration_summary_list
    import aws_sdk_connect.types.next_token


class ListAttachedFilesConfigurationsResponse(TypedDict, closed=True):
    attached_files_configurations: NotRequired[
        "aws_sdk_connect.types.attached_files_configuration_summary_list.AttachedFilesConfigurationSummaryList"
    ]
    """<p>Information about the attached files configurations.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAttachedFilesConfigurationsResponse) -> dict:
    out: dict = {}
    if "attached_files_configurations" in value:
        import aws_sdk_connect.types.attached_files_configuration_summary_list

        out["AttachedFilesConfigurations"] = (
            aws_sdk_connect.types.attached_files_configuration_summary_list.serialize_json(
                value["attached_files_configurations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAttachedFilesConfigurationsResponse:
    out: ListAttachedFilesConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "AttachedFilesConfigurations" in data:
        import aws_sdk_connect.types.attached_files_configuration_summary_list

        out["attached_files_configurations"] = (
            aws_sdk_connect.types.attached_files_configuration_summary_list.deserialize_json(
                data["AttachedFilesConfigurations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
