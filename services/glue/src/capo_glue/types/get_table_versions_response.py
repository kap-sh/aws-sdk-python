"""Generated from Smithy shape ``com.amazonaws.glue#GetTableVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.get_table_versions_list
    import capo_glue.types.token


class GetTableVersionsResponse(TypedDict, closed=True):
    table_versions: NotRequired[
        "capo_glue.types.get_table_versions_list.GetTableVersionsList"
    ]
    """<p>A list of strings identifying available versions of the specified table.</p>"""
    next_token: NotRequired["capo_glue.types.token.Token"]
    """<p>A continuation token, if the list of available versions does not include the last one.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTableVersionsResponse) -> dict:
    out: dict = {}
    if "table_versions" in value:
        import capo_glue.types.get_table_versions_list

        out["TableVersions"] = (
            capo_glue.types.get_table_versions_list.serialize_aws_json_1_1(
                value["table_versions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTableVersionsResponse:
    out: GetTableVersionsResponse = {}  # type: ignore[typeddict-item]
    if "TableVersions" in data:
        import capo_glue.types.get_table_versions_list

        out["table_versions"] = (
            capo_glue.types.get_table_versions_list.deserialize_aws_json_1_1(
                data["TableVersions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
