"""Generated from Smithy shape ``com.amazonaws.taxsettings#TaxRegistrationDocument``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_taxsettings.types.source_s3_location
    import capo_taxsettings.types.tax_registration_doc_file


class TaxRegistrationDocument(TypedDict, closed=True):
    s3_location: NotRequired[
        "capo_taxsettings.types.source_s3_location.SourceS3Location"
    ]
    """<p>The Amazon S3 location where your tax registration document is stored.</p>"""
    file: NotRequired[
        "capo_taxsettings.types.tax_registration_doc_file.TaxRegistrationDocFile"
    ]
    """<p>The tax registration document. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaxRegistrationDocument) -> dict:
    out: dict = {}
    if "s3_location" in value:
        import capo_taxsettings.types.source_s3_location

        out["s3Location"] = capo_taxsettings.types.source_s3_location.serialize_json(
            value["s3_location"]
        )
    if "file" in value:
        import capo_taxsettings.types.tax_registration_doc_file

        out["file"] = capo_taxsettings.types.tax_registration_doc_file.serialize_json(
            value["file"]
        )
    return out


def deserialize_json(data: dict) -> TaxRegistrationDocument:
    out: TaxRegistrationDocument = {}  # type: ignore[typeddict-item]
    if "s3Location" in data:
        import capo_taxsettings.types.source_s3_location

        out["s3_location"] = capo_taxsettings.types.source_s3_location.deserialize_json(
            data["s3Location"]
        )
    if "file" in data:
        import capo_taxsettings.types.tax_registration_doc_file

        out["file"] = capo_taxsettings.types.tax_registration_doc_file.deserialize_json(
            data["file"]
        )
    return out
