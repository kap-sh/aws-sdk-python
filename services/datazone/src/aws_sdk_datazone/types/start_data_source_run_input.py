"""Generated from Smithy shape ``com.amazonaws.datazone#StartDataSourceRunInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.data_source_id
    import aws_sdk_datazone.types.domain_id


class StartDataSourceRunInput(TypedDict, closed=True):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which to start a data source run.</p>"""
    data_source_identifier: "aws_sdk_datazone.types.data_source_id.DataSourceId"
    """<p>The identifier of the data source.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartDataSourceRunInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartDataSourceRunInput:
    out: StartDataSourceRunInput = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
