"""Generated from Smithy shape ``com.amazonaws.glue#JsonClassifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.json_path
    import capo_glue.types.name_string
    import capo_glue.types.timestamp
    import capo_glue.types.version_id


class JsonClassifier(TypedDict, closed=True):
    name: "capo_glue.types.name_string.NameString"
    """<p>The name of the classifier.</p>"""
    creation_time: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The time that this classifier was registered.</p>"""
    last_updated: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The time that this classifier was last updated.</p>"""
    version: "capo_glue.types.version_id.VersionId"
    """<p>The version of this classifier.</p>"""
    json_path: "capo_glue.types.json_path.JsonPath"
    r"""<p>A <code>JsonPath</code> string defining the JSON data for the classifier to classify. Glue supports a subset of JsonPath, as described in <a href=\"https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html#custom-classifier-json\">Writing JsonPath Custom Classifiers</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JsonClassifier) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "creation_time" in value:
        import capo_glue.types.timestamp

        out["CreationTime"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_updated" in value:
        import capo_glue.types.timestamp

        out["LastUpdated"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["last_updated"]
        )
    out["Version"] = value.get("version", 0)
    out["JsonPath"] = value["json_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> JsonClassifier:
    out: JsonClassifier = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("JsonClassifier.name required")
    if "CreationTime" in data:
        import capo_glue.types.timestamp

        out["creation_time"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "LastUpdated" in data:
        import capo_glue.types.timestamp

        out["last_updated"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["LastUpdated"]
        )
    if "Version" in data:
        out["version"] = data["Version"]
    else:
        out["version"] = 0
    if "JsonPath" in data:
        out["json_path"] = data["JsonPath"]
    else:
        raise DeserializationError("JsonClassifier.json_path required")
    return out
