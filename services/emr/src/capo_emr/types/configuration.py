"""Generated from Smithy shape ``com.amazonaws.emr#Configuration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.configuration_list
    import capo_emr.types.string
    import capo_emr.types.string_map


class Configuration(TypedDict, closed=True):
    classification: NotRequired["capo_emr.types.string.String"]
    """<p>The classification within a configuration.</p>"""
    configurations: NotRequired["capo_emr.types.configuration_list.ConfigurationList"]
    """<p>A list of additional configurations to apply within a configuration object.</p>"""
    properties: NotRequired["capo_emr.types.string_map.StringMap"]
    """<p>A set of properties specified within a configuration classification.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Configuration) -> dict:
    out: dict = {}
    if "classification" in value:
        out["Classification"] = value["classification"]
    if "configurations" in value:
        import capo_emr.types.configuration_list

        out["Configurations"] = (
            capo_emr.types.configuration_list.serialize_aws_json_1_1(
                value["configurations"]
            )
        )
    if "properties" in value:
        import capo_emr.types.string_map

        out["Properties"] = capo_emr.types.string_map.serialize_aws_json_1_1(
            value["properties"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Configuration:
    out: Configuration = {}  # type: ignore[typeddict-item]
    if "Classification" in data:
        out["classification"] = data["Classification"]
    if "Configurations" in data:
        import capo_emr.types.configuration_list

        out["configurations"] = (
            capo_emr.types.configuration_list.deserialize_aws_json_1_1(
                data["Configurations"]
            )
        )
    if "Properties" in data:
        import capo_emr.types.string_map

        out["properties"] = capo_emr.types.string_map.deserialize_aws_json_1_1(
            data["Properties"]
        )
    return out
