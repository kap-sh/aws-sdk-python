"""Generated from Smithy shape ``com.amazonaws.ssmsap#ListDatabasesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_sap.types.database_summary_list
    import capo_ssm_sap.types.next_token


class ListDatabasesOutput(TypedDict, closed=True):
    databases: NotRequired[
        "capo_ssm_sap.types.database_summary_list.DatabaseSummaryList"
    ]
    """<p>The SAP HANA databases of an application.</p>"""
    next_token: NotRequired["capo_ssm_sap.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatabasesOutput) -> dict:
    out: dict = {}
    if "databases" in value:
        import capo_ssm_sap.types.database_summary_list

        out["Databases"] = capo_ssm_sap.types.database_summary_list.serialize_json(
            value["databases"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDatabasesOutput:
    out: ListDatabasesOutput = {}  # type: ignore[typeddict-item]
    if "Databases" in data:
        import capo_ssm_sap.types.database_summary_list

        out["databases"] = capo_ssm_sap.types.database_summary_list.deserialize_json(
            data["Databases"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
