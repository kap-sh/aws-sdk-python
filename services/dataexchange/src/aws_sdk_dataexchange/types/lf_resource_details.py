"""Generated from Smithy shape ``com.amazonaws.dataexchange#LFResourceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.database_lf_tag_policy
    import aws_sdk_dataexchange.types.table_lf_tag_policy


class LFResourceDetails(TypedDict, closed=True):
    database: NotRequired[
        "aws_sdk_dataexchange.types.database_lf_tag_policy.DatabaseLFTagPolicy"
    ]
    """<p>Details about the database resource included in the AWS Lake Formation data permission.</p>"""
    table: NotRequired[
        "aws_sdk_dataexchange.types.table_lf_tag_policy.TableLFTagPolicy"
    ]
    """<p>Details about the table resource included in the AWS Lake Formation data permission.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LFResourceDetails) -> dict:
    out: dict = {}
    if "database" in value:
        import aws_sdk_dataexchange.types.database_lf_tag_policy

        out["Database"] = (
            aws_sdk_dataexchange.types.database_lf_tag_policy.serialize_json(
                value["database"]
            )
        )
    if "table" in value:
        import aws_sdk_dataexchange.types.table_lf_tag_policy

        out["Table"] = aws_sdk_dataexchange.types.table_lf_tag_policy.serialize_json(
            value["table"]
        )
    return out


def deserialize_json(data: dict) -> LFResourceDetails:
    out: LFResourceDetails = {}  # type: ignore[typeddict-item]
    if "Database" in data:
        import aws_sdk_dataexchange.types.database_lf_tag_policy

        out["database"] = (
            aws_sdk_dataexchange.types.database_lf_tag_policy.deserialize_json(
                data["Database"]
            )
        )
    if "Table" in data:
        import aws_sdk_dataexchange.types.table_lf_tag_policy

        out["table"] = aws_sdk_dataexchange.types.table_lf_tag_policy.deserialize_json(
            data["Table"]
        )
    return out
