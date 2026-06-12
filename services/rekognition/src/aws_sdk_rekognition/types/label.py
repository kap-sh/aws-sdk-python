"""Generated from Smithy shape ``com.amazonaws.rekognition#Label``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.instances
    import aws_sdk_rekognition.types.label_aliases
    import aws_sdk_rekognition.types.label_categories
    import aws_sdk_rekognition.types.parents
    import aws_sdk_rekognition.types.percent
    import aws_sdk_rekognition.types.string


class Label(TypedDict):
    name: NotRequired["aws_sdk_rekognition.types.string.String"]
    """<p>The name (label) of the object or scene.</p>"""
    confidence: NotRequired["aws_sdk_rekognition.types.percent.Percent"]
    """<p>Level of confidence.</p>"""
    instances: NotRequired["aws_sdk_rekognition.types.instances.Instances"]
    """<p>If <code>Label</code> represents an object, <code>Instances</code> contains the bounding boxes for each instance of the detected object. Bounding boxes are returned for common object labels such as people, cars, furniture, apparel or pets.</p>"""
    parents: NotRequired["aws_sdk_rekognition.types.parents.Parents"]
    """<p>The parent labels for a label. The response includes all ancestor labels.</p>"""
    aliases: NotRequired["aws_sdk_rekognition.types.label_aliases.LabelAliases"]
    """<p>A list of potential aliases for a given label.</p>"""
    categories: NotRequired[
        "aws_sdk_rekognition.types.label_categories.LabelCategories"
    ]
    """<p>A list of the categories associated with a given label.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Label) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    if "instances" in value:
        import aws_sdk_rekognition.types.instances

        out["Instances"] = aws_sdk_rekognition.types.instances.serialize_aws_json_1_1(
            value["instances"]
        )
    if "parents" in value:
        import aws_sdk_rekognition.types.parents

        out["Parents"] = aws_sdk_rekognition.types.parents.serialize_aws_json_1_1(
            value["parents"]
        )
    if "aliases" in value:
        import aws_sdk_rekognition.types.label_aliases

        out["Aliases"] = aws_sdk_rekognition.types.label_aliases.serialize_aws_json_1_1(
            value["aliases"]
        )
    if "categories" in value:
        import aws_sdk_rekognition.types.label_categories

        out["Categories"] = (
            aws_sdk_rekognition.types.label_categories.serialize_aws_json_1_1(
                value["categories"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Label:
    out: Label = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    if "Instances" in data:
        import aws_sdk_rekognition.types.instances

        out["instances"] = aws_sdk_rekognition.types.instances.deserialize_aws_json_1_1(
            data["Instances"]
        )
    if "Parents" in data:
        import aws_sdk_rekognition.types.parents

        out["parents"] = aws_sdk_rekognition.types.parents.deserialize_aws_json_1_1(
            data["Parents"]
        )
    if "Aliases" in data:
        import aws_sdk_rekognition.types.label_aliases

        out["aliases"] = (
            aws_sdk_rekognition.types.label_aliases.deserialize_aws_json_1_1(
                data["Aliases"]
            )
        )
    if "Categories" in data:
        import aws_sdk_rekognition.types.label_categories

        out["categories"] = (
            aws_sdk_rekognition.types.label_categories.deserialize_aws_json_1_1(
                data["Categories"]
            )
        )
    return out
