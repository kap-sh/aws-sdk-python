"""Generated from Smithy shape ``com.amazonaws.glue#CreateClassifierRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.create_csv_classifier_request
    import capo_glue.types.create_grok_classifier_request
    import capo_glue.types.create_json_classifier_request
    import capo_glue.types.create_xml_classifier_request


class CreateClassifierRequest(TypedDict, closed=True):
    grok_classifier: NotRequired[
        "capo_glue.types.create_grok_classifier_request.CreateGrokClassifierRequest"
    ]
    """<p>A <code>GrokClassifier</code> object specifying the classifier to create.</p>"""
    xml_classifier: NotRequired[
        "capo_glue.types.create_xml_classifier_request.CreateXMLClassifierRequest"
    ]
    """<p>An <code>XMLClassifier</code> object specifying the classifier to create.</p>"""
    json_classifier: NotRequired[
        "capo_glue.types.create_json_classifier_request.CreateJsonClassifierRequest"
    ]
    """<p>A <code>JsonClassifier</code> object specifying the classifier to create.</p>"""
    csv_classifier: NotRequired[
        "capo_glue.types.create_csv_classifier_request.CreateCsvClassifierRequest"
    ]
    """<p>A <code>CsvClassifier</code> object specifying the classifier to create.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateClassifierRequest) -> dict:
    out: dict = {}
    if "grok_classifier" in value:
        import capo_glue.types.create_grok_classifier_request

        out["GrokClassifier"] = (
            capo_glue.types.create_grok_classifier_request.serialize_aws_json_1_1(
                value["grok_classifier"]
            )
        )
    if "xml_classifier" in value:
        import capo_glue.types.create_xml_classifier_request

        out["XMLClassifier"] = (
            capo_glue.types.create_xml_classifier_request.serialize_aws_json_1_1(
                value["xml_classifier"]
            )
        )
    if "json_classifier" in value:
        import capo_glue.types.create_json_classifier_request

        out["JsonClassifier"] = (
            capo_glue.types.create_json_classifier_request.serialize_aws_json_1_1(
                value["json_classifier"]
            )
        )
    if "csv_classifier" in value:
        import capo_glue.types.create_csv_classifier_request

        out["CsvClassifier"] = (
            capo_glue.types.create_csv_classifier_request.serialize_aws_json_1_1(
                value["csv_classifier"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateClassifierRequest:
    out: CreateClassifierRequest = {}  # type: ignore[typeddict-item]
    if "GrokClassifier" in data:
        import capo_glue.types.create_grok_classifier_request

        out["grok_classifier"] = (
            capo_glue.types.create_grok_classifier_request.deserialize_aws_json_1_1(
                data["GrokClassifier"]
            )
        )
    if "XMLClassifier" in data:
        import capo_glue.types.create_xml_classifier_request

        out["xml_classifier"] = (
            capo_glue.types.create_xml_classifier_request.deserialize_aws_json_1_1(
                data["XMLClassifier"]
            )
        )
    if "JsonClassifier" in data:
        import capo_glue.types.create_json_classifier_request

        out["json_classifier"] = (
            capo_glue.types.create_json_classifier_request.deserialize_aws_json_1_1(
                data["JsonClassifier"]
            )
        )
    if "CsvClassifier" in data:
        import capo_glue.types.create_csv_classifier_request

        out["csv_classifier"] = (
            capo_glue.types.create_csv_classifier_request.deserialize_aws_json_1_1(
                data["CsvClassifier"]
            )
        )
    return out
