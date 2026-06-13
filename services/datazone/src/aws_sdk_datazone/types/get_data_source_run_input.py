"""Generated from Smithy shape ``com.amazonaws.datazone#GetDataSourceRunInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.data_source_run_id
    import aws_sdk_datazone.types.domain_id


class GetDataSourceRunInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain in which this data source run was performed.</p>"""
    identifier: "aws_sdk_datazone.types.data_source_run_id.DataSourceRunId"
    """<p>The ID of the data source run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataSourceRunInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDataSourceRunInput:
    out: GetDataSourceRunInput = {}  # type: ignore[typeddict-item]
    return out
