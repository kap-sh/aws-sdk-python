"""Generated from Smithy shape ``com.amazonaws.glue#UpdateClassifierRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.update_csv_classifier_request
    import aws_sdk_glue.types.update_grok_classifier_request
    import aws_sdk_glue.types.update_json_classifier_request
    import aws_sdk_glue.types.update_xml_classifier_request


class UpdateClassifierRequest(TypedDict):
    grok_classifier: NotRequired[
        "aws_sdk_glue.types.update_grok_classifier_request.UpdateGrokClassifierRequest"
    ]
    """<p>A <code>GrokClassifier</code> object with updated fields.</p>"""
    xml_classifier: NotRequired[
        "aws_sdk_glue.types.update_xml_classifier_request.UpdateXMLClassifierRequest"
    ]
    """<p>An <code>XMLClassifier</code> object with updated fields.</p>"""
    json_classifier: NotRequired[
        "aws_sdk_glue.types.update_json_classifier_request.UpdateJsonClassifierRequest"
    ]
    """<p>A <code>JsonClassifier</code> object with updated fields.</p>"""
    csv_classifier: NotRequired[
        "aws_sdk_glue.types.update_csv_classifier_request.UpdateCsvClassifierRequest"
    ]
    """<p>A <code>CsvClassifier</code> object with updated fields.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateClassifierRequest) -> dict:
    out: dict = {}
    if "grok_classifier" in value:
        import aws_sdk_glue.types.update_grok_classifier_request

        out["GrokClassifier"] = (
            aws_sdk_glue.types.update_grok_classifier_request.serialize_aws_json_1_1(
                value["grok_classifier"]
            )
        )
    if "xml_classifier" in value:
        import aws_sdk_glue.types.update_xml_classifier_request

        out["XMLClassifier"] = (
            aws_sdk_glue.types.update_xml_classifier_request.serialize_aws_json_1_1(
                value["xml_classifier"]
            )
        )
    if "json_classifier" in value:
        import aws_sdk_glue.types.update_json_classifier_request

        out["JsonClassifier"] = (
            aws_sdk_glue.types.update_json_classifier_request.serialize_aws_json_1_1(
                value["json_classifier"]
            )
        )
    if "csv_classifier" in value:
        import aws_sdk_glue.types.update_csv_classifier_request

        out["CsvClassifier"] = (
            aws_sdk_glue.types.update_csv_classifier_request.serialize_aws_json_1_1(
                value["csv_classifier"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateClassifierRequest:
    out: UpdateClassifierRequest = {}  # type: ignore[typeddict-item]
    if "GrokClassifier" in data:
        import aws_sdk_glue.types.update_grok_classifier_request

        out["grok_classifier"] = (
            aws_sdk_glue.types.update_grok_classifier_request.deserialize_aws_json_1_1(
                data["GrokClassifier"]
            )
        )
    if "XMLClassifier" in data:
        import aws_sdk_glue.types.update_xml_classifier_request

        out["xml_classifier"] = (
            aws_sdk_glue.types.update_xml_classifier_request.deserialize_aws_json_1_1(
                data["XMLClassifier"]
            )
        )
    if "JsonClassifier" in data:
        import aws_sdk_glue.types.update_json_classifier_request

        out["json_classifier"] = (
            aws_sdk_glue.types.update_json_classifier_request.deserialize_aws_json_1_1(
                data["JsonClassifier"]
            )
        )
    if "CsvClassifier" in data:
        import aws_sdk_glue.types.update_csv_classifier_request

        out["csv_classifier"] = (
            aws_sdk_glue.types.update_csv_classifier_request.deserialize_aws_json_1_1(
                data["CsvClassifier"]
            )
        )
    return out
