"""Generated from Smithy shape ``com.amazonaws.datazone#GetDataSourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.data_source_id
    import aws_sdk_datazone.types.domain_id


class GetDataSourceInput(TypedDict, closed=True):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the data source exists.</p>"""
    identifier: "aws_sdk_datazone.types.data_source_id.DataSourceId"
    """<p>The ID of the Amazon DataZone data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataSourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDataSourceInput:
    out: GetDataSourceInput = {}  # type: ignore[typeddict-item]
    return out
