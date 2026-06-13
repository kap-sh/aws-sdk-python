"""Generated from Smithy shape ``com.amazonaws.emr#Configuration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.configuration_list
    import aws_sdk_emr.types.string
    import aws_sdk_emr.types.string_map


class Configuration(TypedDict):
    classification: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The classification within a configuration.</p>"""
    configurations: NotRequired[
        "aws_sdk_emr.types.configuration_list.ConfigurationList"
    ]
    """<p>A list of additional configurations to apply within a configuration object.</p>"""
    properties: NotRequired["aws_sdk_emr.types.string_map.StringMap"]
    """<p>A set of properties specified within a configuration classification.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Configuration) -> dict:
    out: dict = {}
    if "classification" in value:
        out["Classification"] = value["classification"]
    if "configurations" in value:
        import aws_sdk_emr.types.configuration_list

        out["Configurations"] = (
            aws_sdk_emr.types.configuration_list.serialize_aws_json_1_1(
                value["configurations"]
            )
        )
    if "properties" in value:
        import aws_sdk_emr.types.string_map

        out["Properties"] = aws_sdk_emr.types.string_map.serialize_aws_json_1_1(
            value["properties"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Configuration:
    out: Configuration = {}  # type: ignore[typeddict-item]
    if "Classification" in data:
        out["classification"] = data["Classification"]
    if "Configurations" in data:
        import aws_sdk_emr.types.configuration_list

        out["configurations"] = (
            aws_sdk_emr.types.configuration_list.deserialize_aws_json_1_1(
                data["Configurations"]
            )
        )
    if "Properties" in data:
        import aws_sdk_emr.types.string_map

        out["properties"] = aws_sdk_emr.types.string_map.deserialize_aws_json_1_1(
            data["Properties"]
        )
    return out
