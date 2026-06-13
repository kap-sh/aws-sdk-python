"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteDataExportConfigurationInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id


class DeleteDataExportConfigurationInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The domain ID for which you want to delete the data export configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataExportConfigurationInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDataExportConfigurationInput:
    out: DeleteDataExportConfigurationInput = {}  # type: ignore[typeddict-item]
    return out
