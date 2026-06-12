"""Generated from Smithy shape ``com.amazonaws.appstream#ListEntitledApplicationsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.entitled_application_list
    import aws_sdk_appstream.types.string


class ListEntitledApplicationsResult(TypedDict):
    entitled_applications: NotRequired[
        "aws_sdk_appstream.types.entitled_application_list.EntitledApplicationList"
    ]
    """<p>The entitled applications.</p>"""
    next_token: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEntitledApplicationsResult) -> dict:
    out: dict = {}
    if "entitled_applications" in value:
        import aws_sdk_appstream.types.entitled_application_list

        out["EntitledApplications"] = (
            aws_sdk_appstream.types.entitled_application_list.serialize_aws_json_1_1(
                value["entitled_applications"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEntitledApplicationsResult:
    out: ListEntitledApplicationsResult = {}  # type: ignore[typeddict-item]
    if "EntitledApplications" in data:
        import aws_sdk_appstream.types.entitled_application_list

        out["entitled_applications"] = (
            aws_sdk_appstream.types.entitled_application_list.deserialize_aws_json_1_1(
                data["EntitledApplications"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
