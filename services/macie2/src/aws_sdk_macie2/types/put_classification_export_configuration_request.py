"""Generated from Smithy shape ``com.amazonaws.macie2#PutClassificationExportConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.classification_export_configuration


class PutClassificationExportConfigurationRequest(TypedDict, closed=True):
    configuration: NotRequired[
        "aws_sdk_macie2.types.classification_export_configuration.ClassificationExportConfiguration"
    ]
    """<p>The location to store data classification results in, and the encryption settings to use when storing results in that location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutClassificationExportConfigurationRequest) -> dict:
    out: dict = {}
    if "configuration" in value:
        import aws_sdk_macie2.types.classification_export_configuration

        out["configuration"] = (
            aws_sdk_macie2.types.classification_export_configuration.serialize_json(
                value["configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutClassificationExportConfigurationRequest:
    out: PutClassificationExportConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "configuration" in data:
        import aws_sdk_macie2.types.classification_export_configuration

        out["configuration"] = (
            aws_sdk_macie2.types.classification_export_configuration.deserialize_json(
                data["configuration"]
            )
        )
    return out
