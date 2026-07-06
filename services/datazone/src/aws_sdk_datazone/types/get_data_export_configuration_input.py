"""Generated from Smithy shape ``com.amazonaws.datazone#GetDataExportConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id


class GetDataExportConfigurationInput(TypedDict, closed=True):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where you want to get the data export configuration details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataExportConfigurationInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDataExportConfigurationInput:
    out: GetDataExportConfigurationInput = {}  # type: ignore[typeddict-item]
    return out
