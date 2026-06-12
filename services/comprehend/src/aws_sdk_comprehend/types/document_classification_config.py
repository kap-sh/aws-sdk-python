"""Generated from Smithy shape ``com.amazonaws.comprehend#DocumentClassificationConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.document_classifier_mode
    import aws_sdk_comprehend.types.labels_list


class DocumentClassificationConfig(TypedDict):
    mode: "aws_sdk_comprehend.types.document_classifier_mode.DocumentClassifierMode"
    """<p>Classification mode indicates whether the documents are <code>MULTI_CLASS</code> or <code>MULTI_LABEL</code>.</p>"""
    labels: NotRequired["aws_sdk_comprehend.types.labels_list.LabelsList"]
    """<p>One or more labels to associate with the custom classifier.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentClassificationConfig) -> dict:
    out: dict = {}
    import aws_sdk_comprehend.types.document_classifier_mode

    out["Mode"] = (
        aws_sdk_comprehend.types.document_classifier_mode.serialize_aws_json_1_1(
            value["mode"]
        )
    )
    if "labels" in value:
        import aws_sdk_comprehend.types.labels_list

        out["Labels"] = aws_sdk_comprehend.types.labels_list.serialize_aws_json_1_1(
            value["labels"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentClassificationConfig:
    out: DocumentClassificationConfig = {}  # type: ignore[typeddict-item]
    if "Mode" in data:
        import aws_sdk_comprehend.types.document_classifier_mode

        out["mode"] = (
            aws_sdk_comprehend.types.document_classifier_mode.deserialize_aws_json_1_1(
                data["Mode"]
            )
        )
    else:
        raise DeserializationError("DocumentClassificationConfig.mode required")
    if "Labels" in data:
        import aws_sdk_comprehend.types.labels_list

        out["labels"] = aws_sdk_comprehend.types.labels_list.deserialize_aws_json_1_1(
            data["Labels"]
        )
    return out
