"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTableRecordExpirationConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.table_arn


class GetTableRecordExpirationConfigurationRequest(TypedDict):
    table_arn: "aws_sdk_s3tables.types.table_arn.TableARN"
    """<p>The Amazon Resource Name (ARN) of the table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableRecordExpirationConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTableRecordExpirationConfigurationRequest:
    out: GetTableRecordExpirationConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
