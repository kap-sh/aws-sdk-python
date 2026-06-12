"""Generated from Smithy shape ``com.amazonaws.glue#Mapping``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.boxed_boolean
    import aws_sdk_glue.types.enclosed_in_string_properties
    import aws_sdk_glue.types.enclosed_in_string_property
    import aws_sdk_glue.types.mappings


class Mapping(TypedDict):
    to_key: NotRequired[
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>After the apply mapping, what the name of the column should be. Can be the same as <code>FromPath</code>.</p>"""
    from_path: NotRequired[
        "aws_sdk_glue.types.enclosed_in_string_properties.EnclosedInStringProperties"
    ]
    """<p>The table or column to be modified.</p>"""
    from_type: NotRequired[
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The type of the data to be modified.</p>"""
    to_type: NotRequired[
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The data type that the data is to be modified to.</p>"""
    dropped: NotRequired["aws_sdk_glue.types.boxed_boolean.BoxedBoolean"]
    """<p>If true, then the column is removed.</p>"""
    children: NotRequired["aws_sdk_glue.types.mappings.Mappings"]
    """<p>Only applicable to nested data structures. If you want to change the parent structure, but also one of its children, you can fill out this data strucutre. It is also <code>Mapping</code>, but its <code>FromPath</code> will be the parent's <code>FromPath</code> plus the <code>FromPath</code> from this structure.</p> <p>For the children part, suppose you have the structure:</p> <p> <code>{ \"FromPath\": \"OuterStructure\", \"ToKey\": \"OuterStructure\", \"ToType\": \"Struct\", \"Dropped\": false, \"Chidlren\": [{ \"FromPath\": \"inner\", \"ToKey\": \"inner\", \"ToType\": \"Double\", \"Dropped\": false, }] }</code> </p> <p>You can specify a <code>Mapping</code> that looks like:</p> <p> <code>{ \"FromPath\": \"OuterStructure\", \"ToKey\": \"OuterStructure\", \"ToType\": \"Struct\", \"Dropped\": false, \"Chidlren\": [{ \"FromPath\": \"inner\", \"ToKey\": \"inner\", \"ToType\": \"Double\", \"Dropped\": false, }] }</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Mapping) -> dict:
    out: dict = {}
    if "to_key" in value:
        out["ToKey"] = value["to_key"]
    if "from_path" in value:
        import aws_sdk_glue.types.enclosed_in_string_properties

        out["FromPath"] = (
            aws_sdk_glue.types.enclosed_in_string_properties.serialize_aws_json_1_1(
                value["from_path"]
            )
        )
    if "from_type" in value:
        out["FromType"] = value["from_type"]
    if "to_type" in value:
        out["ToType"] = value["to_type"]
    if "dropped" in value:
        out["Dropped"] = value["dropped"]
    if "children" in value:
        import aws_sdk_glue.types.mappings

        out["Children"] = aws_sdk_glue.types.mappings.serialize_aws_json_1_1(
            value["children"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Mapping:
    out: Mapping = {}  # type: ignore[typeddict-item]
    if "ToKey" in data:
        out["to_key"] = data["ToKey"]
    if "FromPath" in data:
        import aws_sdk_glue.types.enclosed_in_string_properties

        out["from_path"] = (
            aws_sdk_glue.types.enclosed_in_string_properties.deserialize_aws_json_1_1(
                data["FromPath"]
            )
        )
    if "FromType" in data:
        out["from_type"] = data["FromType"]
    if "ToType" in data:
        out["to_type"] = data["ToType"]
    if "Dropped" in data:
        out["dropped"] = data["Dropped"]
    if "Children" in data:
        import aws_sdk_glue.types.mappings

        out["children"] = aws_sdk_glue.types.mappings.deserialize_aws_json_1_1(
            data["Children"]
        )
    return out
