"""Generated from Smithy shape ``com.amazonaws.athena#Classification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.name_string
    import capo_athena.types.parameters_map


class Classification(TypedDict, closed=True):
    name: NotRequired["capo_athena.types.name_string.NameString"]
    """<p>The name of the configuration classification.</p>"""
    properties: NotRequired["capo_athena.types.parameters_map.ParametersMap"]
    """<p>A set of properties specified within a configuration classification.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Classification) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "properties" in value:
        import capo_athena.types.parameters_map

        out["Properties"] = capo_athena.types.parameters_map.serialize_aws_json_1_1(
            value["properties"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Classification:
    out: Classification = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Properties" in data:
        import capo_athena.types.parameters_map

        out["properties"] = capo_athena.types.parameters_map.deserialize_aws_json_1_1(
            data["Properties"]
        )
    return out
