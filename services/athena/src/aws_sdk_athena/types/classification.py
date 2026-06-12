"""Generated from Smithy shape ``com.amazonaws.athena#Classification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_athena.types.name_string
    import aws_sdk_athena.types.parameters_map


class Classification(TypedDict):
    name: NotRequired["aws_sdk_athena.types.name_string.NameString"]
    """<p>The name of the configuration classification.</p>"""
    properties: NotRequired["aws_sdk_athena.types.parameters_map.ParametersMap"]
    """<p>A set of properties specified within a configuration classification.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Classification) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "properties" in value:
        import aws_sdk_athena.types.parameters_map

        out["Properties"] = aws_sdk_athena.types.parameters_map.serialize_aws_json_1_1(
            value["properties"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Classification:
    out: Classification = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Properties" in data:
        import aws_sdk_athena.types.parameters_map

        out["properties"] = (
            aws_sdk_athena.types.parameters_map.deserialize_aws_json_1_1(
                data["Properties"]
            )
        )
    return out
