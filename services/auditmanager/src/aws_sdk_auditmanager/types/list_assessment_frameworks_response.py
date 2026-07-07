"""Generated from Smithy shape ``com.amazonaws.auditmanager#ListAssessmentFrameworksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.framework_metadata_list
    import aws_sdk_auditmanager.types.token


class ListAssessmentFrameworksResponse(TypedDict, closed=True):
    framework_metadata_list: NotRequired[
        "aws_sdk_auditmanager.types.framework_metadata_list.FrameworkMetadataList"
    ]
    """<p> A list of metadata that the <code>ListAssessmentFrameworks</code> API returns for each framework.</p>"""
    next_token: NotRequired["aws_sdk_auditmanager.types.token.Token"]
    """<p> The pagination token that's used to fetch the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssessmentFrameworksResponse) -> dict:
    out: dict = {}
    if "framework_metadata_list" in value:
        import aws_sdk_auditmanager.types.framework_metadata_list

        out["frameworkMetadataList"] = (
            aws_sdk_auditmanager.types.framework_metadata_list.serialize_json(
                value["framework_metadata_list"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssessmentFrameworksResponse:
    out: ListAssessmentFrameworksResponse = {}  # type: ignore[typeddict-item]
    if "frameworkMetadataList" in data:
        import aws_sdk_auditmanager.types.framework_metadata_list

        out["framework_metadata_list"] = (
            aws_sdk_auditmanager.types.framework_metadata_list.deserialize_json(
                data["frameworkMetadataList"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
