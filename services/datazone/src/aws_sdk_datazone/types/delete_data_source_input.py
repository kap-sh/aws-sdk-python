"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteDataSourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.data_source_id
    import aws_sdk_datazone.types.domain_id


class DeleteDataSourceInput(TypedDict, closed=True):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the data source is deleted.</p>"""
    identifier: "aws_sdk_datazone.types.data_source_id.DataSourceId"
    """<p>The identifier of the data source that is deleted.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""
    retain_permissions_on_revoke_failure: NotRequired["bool"]
    """<p>Specifies that the granted permissions are retained in case of a self-subscribe functionality failure for a data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataSourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDataSourceInput:
    out: DeleteDataSourceInput = {}  # type: ignore[typeddict-item]
    return out
