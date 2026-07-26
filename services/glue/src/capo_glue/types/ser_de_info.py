"""Generated from Smithy shape ``com.amazonaws.glue#SerDeInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.name_string
    import capo_glue.types.parameters_map


class SerDeInfo(TypedDict, closed=True):
    name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>Name of the SerDe.</p>"""
    serialization_library: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>Usually the class that implements the SerDe. An example is <code>org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe</code>.</p>"""
    parameters: NotRequired["capo_glue.types.parameters_map.ParametersMap"]
    """<p>These key-value pairs define initialization parameters for the SerDe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SerDeInfo) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "serialization_library" in value:
        out["SerializationLibrary"] = value["serialization_library"]
    if "parameters" in value:
        import capo_glue.types.parameters_map

        out["Parameters"] = capo_glue.types.parameters_map.serialize_aws_json_1_1(
            value["parameters"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SerDeInfo:
    out: SerDeInfo = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "SerializationLibrary" in data:
        out["serialization_library"] = data["SerializationLibrary"]
    if "Parameters" in data:
        import capo_glue.types.parameters_map

        out["parameters"] = capo_glue.types.parameters_map.deserialize_aws_json_1_1(
            data["Parameters"]
        )
    return out
