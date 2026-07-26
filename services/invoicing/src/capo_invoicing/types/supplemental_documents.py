"""Generated from Smithy shape ``com.amazonaws.invoicing#SupplementalDocuments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_invoicing.types.supplemental_document

SupplementalDocuments: TypeAlias = list[
    "capo_invoicing.types.supplemental_document.SupplementalDocument"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SupplementalDocuments) -> list:
    import capo_invoicing.types.supplemental_document

    out: list = []
    for item in value:
        out.append(
            capo_invoicing.types.supplemental_document.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SupplementalDocuments:
    import capo_invoicing.types.supplemental_document

    out: SupplementalDocuments = []
    for item in data:
        out.append(
            capo_invoicing.types.supplemental_document.deserialize_aws_json_1_0(item)
        )
    return out
