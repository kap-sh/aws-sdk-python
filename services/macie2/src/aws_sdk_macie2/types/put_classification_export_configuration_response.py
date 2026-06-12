"""Generated from Smithy shape ``com.amazonaws.macie2#PutClassificationExportConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.classification_export_configuration


class PutClassificationExportConfigurationResponse(TypedDict):
    configuration: NotRequired[
        "aws_sdk_macie2.types.classification_export_configuration.ClassificationExportConfiguration"
    ]
    """<p>The location where the data classification results are stored, and the encryption settings that are used when storing results in that location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutClassificationExportConfigurationResponse) -> dict:
    out: dict = {}
    if "configuration" in value:
        import aws_sdk_macie2.types.classification_export_configuration

        out["configuration"] = (
            aws_sdk_macie2.types.classification_export_configuration.serialize_json(
                value["configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutClassificationExportConfigurationResponse:
    out: PutClassificationExportConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "configuration" in data:
        import aws_sdk_macie2.types.classification_export_configuration

        out["configuration"] = (
            aws_sdk_macie2.types.classification_export_configuration.deserialize_json(
                data["configuration"]
            )
        )
    return out
