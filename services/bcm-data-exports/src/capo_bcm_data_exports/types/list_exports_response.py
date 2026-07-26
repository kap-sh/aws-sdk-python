"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#ListExportsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_data_exports.types.export_reference_list
    import capo_bcm_data_exports.types.next_page_token


class ListExportsResponse(TypedDict, closed=True):
    exports: NotRequired[
        "capo_bcm_data_exports.types.export_reference_list.ExportReferenceList"
    ]
    """<p>The details of the exports, including name and export status.</p>"""
    next_token: NotRequired["capo_bcm_data_exports.types.next_page_token.NextPageToken"]
    """<p>The token to retrieve the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListExportsResponse) -> dict:
    out: dict = {}
    if "exports" in value:
        import capo_bcm_data_exports.types.export_reference_list

        out["Exports"] = (
            capo_bcm_data_exports.types.export_reference_list.serialize_aws_json_1_1(
                value["exports"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListExportsResponse:
    out: ListExportsResponse = {}  # type: ignore[typeddict-item]
    if "Exports" in data:
        import capo_bcm_data_exports.types.export_reference_list

        out["exports"] = (
            capo_bcm_data_exports.types.export_reference_list.deserialize_aws_json_1_1(
                data["Exports"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
