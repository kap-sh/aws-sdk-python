"""Generated from Smithy shape ``com.amazonaws.dataexchange#LFResourceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.database_lf_tag_policy
    import capo_dataexchange.types.table_lf_tag_policy


class LFResourceDetails(TypedDict, closed=True):
    database: NotRequired[
        "capo_dataexchange.types.database_lf_tag_policy.DatabaseLFTagPolicy"
    ]
    """<p>Details about the database resource included in the AWS Lake Formation data permission.</p>"""
    table: NotRequired["capo_dataexchange.types.table_lf_tag_policy.TableLFTagPolicy"]
    """<p>Details about the table resource included in the AWS Lake Formation data permission.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LFResourceDetails) -> dict:
    out: dict = {}
    if "database" in value:
        import capo_dataexchange.types.database_lf_tag_policy

        out["Database"] = capo_dataexchange.types.database_lf_tag_policy.serialize_json(
            value["database"]
        )
    if "table" in value:
        import capo_dataexchange.types.table_lf_tag_policy

        out["Table"] = capo_dataexchange.types.table_lf_tag_policy.serialize_json(
            value["table"]
        )
    return out


def deserialize_json(data: dict) -> LFResourceDetails:
    out: LFResourceDetails = {}  # type: ignore[typeddict-item]
    if "Database" in data:
        import capo_dataexchange.types.database_lf_tag_policy

        out["database"] = (
            capo_dataexchange.types.database_lf_tag_policy.deserialize_json(
                data["Database"]
            )
        )
    if "Table" in data:
        import capo_dataexchange.types.table_lf_tag_policy

        out["table"] = capo_dataexchange.types.table_lf_tag_policy.deserialize_json(
            data["Table"]
        )
    return out
