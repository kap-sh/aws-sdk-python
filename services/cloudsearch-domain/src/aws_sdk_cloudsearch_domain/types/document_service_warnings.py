"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#DocumentServiceWarnings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudsearch_domain.types.document_service_warning

DocumentServiceWarnings: TypeAlias = list[
    "aws_sdk_cloudsearch_domain.types.document_service_warning.DocumentServiceWarning"
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentServiceWarnings) -> list:
    import aws_sdk_cloudsearch_domain.types.document_service_warning

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudsearch_domain.types.document_service_warning.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DocumentServiceWarnings:
    import aws_sdk_cloudsearch_domain.types.document_service_warning

    out: DocumentServiceWarnings = []
    for item in data:
        out.append(
            aws_sdk_cloudsearch_domain.types.document_service_warning.deserialize_json(
                item
            )
        )
    return out
