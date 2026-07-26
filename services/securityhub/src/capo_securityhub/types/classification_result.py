"""Generated from Smithy shape ``com.amazonaws.securityhub#ClassificationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.classification_status
    import capo_securityhub.types.custom_data_identifiers_result
    import capo_securityhub.types.long
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.sensitive_data_result_list


class ClassificationResult(TypedDict, closed=True):
    mime_type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of content that the finding applies to.</p>"""
    size_classified: NotRequired["capo_securityhub.types.long.Long"]
    """<p>The total size in bytes of the affected data.</p>"""
    additional_occurrences: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether there are additional occurrences of sensitive data that are not included in the finding. This occurs when the number of occurrences exceeds the maximum that can be included.</p>"""
    status: NotRequired[
        "capo_securityhub.types.classification_status.ClassificationStatus"
    ]
    """<p>The current status of the sensitive data detection.</p>"""
    sensitive_data: NotRequired[
        "capo_securityhub.types.sensitive_data_result_list.SensitiveDataResultList"
    ]
    """<p>Provides details about sensitive data that was identified based on built-in configuration.</p>"""
    custom_data_identifiers: NotRequired[
        "capo_securityhub.types.custom_data_identifiers_result.CustomDataIdentifiersResult"
    ]
    """<p>Provides details about sensitive data that was identified based on customer-defined configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClassificationResult) -> dict:
    out: dict = {}
    if "mime_type" in value:
        out["MimeType"] = value["mime_type"]
    if "size_classified" in value:
        out["SizeClassified"] = value["size_classified"]
    if "additional_occurrences" in value:
        out["AdditionalOccurrences"] = value["additional_occurrences"]
    if "status" in value:
        import capo_securityhub.types.classification_status

        out["Status"] = capo_securityhub.types.classification_status.serialize_json(
            value["status"]
        )
    if "sensitive_data" in value:
        import capo_securityhub.types.sensitive_data_result_list

        out["SensitiveData"] = (
            capo_securityhub.types.sensitive_data_result_list.serialize_json(
                value["sensitive_data"]
            )
        )
    if "custom_data_identifiers" in value:
        import capo_securityhub.types.custom_data_identifiers_result

        out["CustomDataIdentifiers"] = (
            capo_securityhub.types.custom_data_identifiers_result.serialize_json(
                value["custom_data_identifiers"]
            )
        )
    return out


def deserialize_json(data: dict) -> ClassificationResult:
    out: ClassificationResult = {}  # type: ignore[typeddict-item]
    if "MimeType" in data:
        out["mime_type"] = data["MimeType"]
    if "SizeClassified" in data:
        out["size_classified"] = data["SizeClassified"]
    if "AdditionalOccurrences" in data:
        out["additional_occurrences"] = data["AdditionalOccurrences"]
    if "Status" in data:
        import capo_securityhub.types.classification_status

        out["status"] = capo_securityhub.types.classification_status.deserialize_json(
            data["Status"]
        )
    if "SensitiveData" in data:
        import capo_securityhub.types.sensitive_data_result_list

        out["sensitive_data"] = (
            capo_securityhub.types.sensitive_data_result_list.deserialize_json(
                data["SensitiveData"]
            )
        )
    if "CustomDataIdentifiers" in data:
        import capo_securityhub.types.custom_data_identifiers_result

        out["custom_data_identifiers"] = (
            capo_securityhub.types.custom_data_identifiers_result.deserialize_json(
                data["CustomDataIdentifiers"]
            )
        )
    return out
