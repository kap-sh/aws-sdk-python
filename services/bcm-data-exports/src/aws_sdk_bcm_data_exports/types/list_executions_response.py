"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#ListExecutionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bcm_data_exports.types.execution_reference_list
    import aws_sdk_bcm_data_exports.types.next_page_token


class ListExecutionsResponse(TypedDict, closed=True):
    executions: NotRequired[
        "aws_sdk_bcm_data_exports.types.execution_reference_list.ExecutionReferenceList"
    ]
    """<p>The list of executions.</p>"""
    next_token: NotRequired[
        "aws_sdk_bcm_data_exports.types.next_page_token.NextPageToken"
    ]
    """<p>The token to retrieve the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListExecutionsResponse) -> dict:
    out: dict = {}
    if "executions" in value:
        import aws_sdk_bcm_data_exports.types.execution_reference_list

        out["Executions"] = (
            aws_sdk_bcm_data_exports.types.execution_reference_list.serialize_aws_json_1_1(
                value["executions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListExecutionsResponse:
    out: ListExecutionsResponse = {}  # type: ignore[typeddict-item]
    if "Executions" in data:
        import aws_sdk_bcm_data_exports.types.execution_reference_list

        out["executions"] = (
            aws_sdk_bcm_data_exports.types.execution_reference_list.deserialize_aws_json_1_1(
                data["Executions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
