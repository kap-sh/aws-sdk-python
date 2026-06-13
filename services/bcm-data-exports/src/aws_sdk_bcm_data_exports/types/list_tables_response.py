"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#ListTablesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bcm_data_exports.types.next_page_token
    import aws_sdk_bcm_data_exports.types.table_list


class ListTablesResponse(TypedDict):
    tables: NotRequired["aws_sdk_bcm_data_exports.types.table_list.TableList"]
    """<p>The list of tables.</p>"""
    next_token: NotRequired[
        "aws_sdk_bcm_data_exports.types.next_page_token.NextPageToken"
    ]
    """<p>The token to retrieve the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTablesResponse) -> dict:
    out: dict = {}
    if "tables" in value:
        import aws_sdk_bcm_data_exports.types.table_list

        out["Tables"] = (
            aws_sdk_bcm_data_exports.types.table_list.serialize_aws_json_1_1(
                value["tables"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTablesResponse:
    out: ListTablesResponse = {}  # type: ignore[typeddict-item]
    if "Tables" in data:
        import aws_sdk_bcm_data_exports.types.table_list

        out["tables"] = (
            aws_sdk_bcm_data_exports.types.table_list.deserialize_aws_json_1_1(
                data["Tables"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
