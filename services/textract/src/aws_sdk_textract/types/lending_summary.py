"""Generated from Smithy shape ``com.amazonaws.textract#LendingSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_textract.types.document_group_list
    import aws_sdk_textract.types.undetected_document_type_list


class LendingSummary(TypedDict):
    document_groups: NotRequired[
        "aws_sdk_textract.types.document_group_list.DocumentGroupList"
    ]
    """<p>Contains an array of all DocumentGroup objects.</p>"""
    undetected_document_types: NotRequired[
        "aws_sdk_textract.types.undetected_document_type_list.UndetectedDocumentTypeList"
    ]
    """<p>UndetectedDocumentTypes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LendingSummary) -> dict:
    out: dict = {}
    if "document_groups" in value:
        import aws_sdk_textract.types.document_group_list

        out["DocumentGroups"] = (
            aws_sdk_textract.types.document_group_list.serialize_aws_json_1_1(
                value["document_groups"]
            )
        )
    if "undetected_document_types" in value:
        import aws_sdk_textract.types.undetected_document_type_list

        out["UndetectedDocumentTypes"] = (
            aws_sdk_textract.types.undetected_document_type_list.serialize_aws_json_1_1(
                value["undetected_document_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LendingSummary:
    out: LendingSummary = {}  # type: ignore[typeddict-item]
    if "DocumentGroups" in data:
        import aws_sdk_textract.types.document_group_list

        out["document_groups"] = (
            aws_sdk_textract.types.document_group_list.deserialize_aws_json_1_1(
                data["DocumentGroups"]
            )
        )
    if "UndetectedDocumentTypes" in data:
        import aws_sdk_textract.types.undetected_document_type_list

        out["undetected_document_types"] = (
            aws_sdk_textract.types.undetected_document_type_list.deserialize_aws_json_1_1(
                data["UndetectedDocumentTypes"]
            )
        )
    return out
