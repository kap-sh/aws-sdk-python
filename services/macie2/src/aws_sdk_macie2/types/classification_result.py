"""Generated from Smithy shape ``com.amazonaws.macie2#ClassificationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__boolean
    import aws_sdk_macie2.types.__long
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.classification_result_status
    import aws_sdk_macie2.types.custom_data_identifiers
    import aws_sdk_macie2.types.sensitive_data


class ClassificationResult(TypedDict, closed=True):
    additional_occurrences: NotRequired["aws_sdk_macie2.types.__boolean.__boolean"]
    """<p>Specifies whether Amazon Macie detected additional occurrences of sensitive data in the S3 object. A finding includes location data for a maximum of 15 occurrences of sensitive data.</p> <p>This value can help you determine whether to investigate additional occurrences of sensitive data in an object. You can do this by referring to the corresponding sensitive data discovery result for the finding (classificationDetails.detailedResultsLocation).</p>"""
    custom_data_identifiers: NotRequired[
        "aws_sdk_macie2.types.custom_data_identifiers.CustomDataIdentifiers"
    ]
    """<p>The custom data identifiers that detected the sensitive data and the number of occurrences of the data that they detected.</p>"""
    mime_type: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The type of content, as a MIME type, that the finding applies to. For example, application/gzip, for a GNU Gzip compressed archive file, or application/pdf, for an Adobe Portable Document Format file.</p>"""
    sensitive_data: NotRequired["aws_sdk_macie2.types.sensitive_data.SensitiveData"]
    """<p>The category, types, and number of occurrences of the sensitive data that produced the finding.</p>"""
    size_classified: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total size, in bytes, of the data that the finding applies to.</p>"""
    status: NotRequired[
        "aws_sdk_macie2.types.classification_result_status.ClassificationResultStatus"
    ]
    """<p>The status of the finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClassificationResult) -> dict:
    out: dict = {}
    if "additional_occurrences" in value:
        out["additionalOccurrences"] = value["additional_occurrences"]
    if "custom_data_identifiers" in value:
        import aws_sdk_macie2.types.custom_data_identifiers

        out["customDataIdentifiers"] = (
            aws_sdk_macie2.types.custom_data_identifiers.serialize_json(
                value["custom_data_identifiers"]
            )
        )
    if "mime_type" in value:
        out["mimeType"] = value["mime_type"]
    if "sensitive_data" in value:
        import aws_sdk_macie2.types.sensitive_data

        out["sensitiveData"] = aws_sdk_macie2.types.sensitive_data.serialize_json(
            value["sensitive_data"]
        )
    if "size_classified" in value:
        out["sizeClassified"] = value["size_classified"]
    if "status" in value:
        import aws_sdk_macie2.types.classification_result_status

        out["status"] = (
            aws_sdk_macie2.types.classification_result_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> ClassificationResult:
    out: ClassificationResult = {}  # type: ignore[typeddict-item]
    if "additionalOccurrences" in data:
        out["additional_occurrences"] = data["additionalOccurrences"]
    if "customDataIdentifiers" in data:
        import aws_sdk_macie2.types.custom_data_identifiers

        out["custom_data_identifiers"] = (
            aws_sdk_macie2.types.custom_data_identifiers.deserialize_json(
                data["customDataIdentifiers"]
            )
        )
    if "mimeType" in data:
        out["mime_type"] = data["mimeType"]
    if "sensitiveData" in data:
        import aws_sdk_macie2.types.sensitive_data

        out["sensitive_data"] = aws_sdk_macie2.types.sensitive_data.deserialize_json(
            data["sensitiveData"]
        )
    if "sizeClassified" in data:
        out["size_classified"] = data["sizeClassified"]
    if "status" in data:
        import aws_sdk_macie2.types.classification_result_status

        out["status"] = (
            aws_sdk_macie2.types.classification_result_status.deserialize_json(
                data["status"]
            )
        )
    return out
