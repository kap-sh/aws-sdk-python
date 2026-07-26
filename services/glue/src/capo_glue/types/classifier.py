"""Generated from Smithy shape ``com.amazonaws.glue#Classifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.csv_classifier
    import capo_glue.types.grok_classifier
    import capo_glue.types.json_classifier
    import capo_glue.types.xml_classifier


class Classifier(TypedDict, closed=True):
    grok_classifier: NotRequired["capo_glue.types.grok_classifier.GrokClassifier"]
    """<p>A classifier that uses <code>grok</code>.</p>"""
    xml_classifier: NotRequired["capo_glue.types.xml_classifier.XMLClassifier"]
    """<p>A classifier for XML content.</p>"""
    json_classifier: NotRequired["capo_glue.types.json_classifier.JsonClassifier"]
    """<p>A classifier for JSON content.</p>"""
    csv_classifier: NotRequired["capo_glue.types.csv_classifier.CsvClassifier"]
    """<p>A classifier for comma-separated values (CSV).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Classifier) -> dict:
    out: dict = {}
    if "grok_classifier" in value:
        import capo_glue.types.grok_classifier

        out["GrokClassifier"] = capo_glue.types.grok_classifier.serialize_aws_json_1_1(
            value["grok_classifier"]
        )
    if "xml_classifier" in value:
        import capo_glue.types.xml_classifier

        out["XMLClassifier"] = capo_glue.types.xml_classifier.serialize_aws_json_1_1(
            value["xml_classifier"]
        )
    if "json_classifier" in value:
        import capo_glue.types.json_classifier

        out["JsonClassifier"] = capo_glue.types.json_classifier.serialize_aws_json_1_1(
            value["json_classifier"]
        )
    if "csv_classifier" in value:
        import capo_glue.types.csv_classifier

        out["CsvClassifier"] = capo_glue.types.csv_classifier.serialize_aws_json_1_1(
            value["csv_classifier"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Classifier:
    out: Classifier = {}  # type: ignore[typeddict-item]
    if "GrokClassifier" in data:
        import capo_glue.types.grok_classifier

        out["grok_classifier"] = (
            capo_glue.types.grok_classifier.deserialize_aws_json_1_1(
                data["GrokClassifier"]
            )
        )
    if "XMLClassifier" in data:
        import capo_glue.types.xml_classifier

        out["xml_classifier"] = capo_glue.types.xml_classifier.deserialize_aws_json_1_1(
            data["XMLClassifier"]
        )
    if "JsonClassifier" in data:
        import capo_glue.types.json_classifier

        out["json_classifier"] = (
            capo_glue.types.json_classifier.deserialize_aws_json_1_1(
                data["JsonClassifier"]
            )
        )
    if "CsvClassifier" in data:
        import capo_glue.types.csv_classifier

        out["csv_classifier"] = capo_glue.types.csv_classifier.deserialize_aws_json_1_1(
            data["CsvClassifier"]
        )
    return out
