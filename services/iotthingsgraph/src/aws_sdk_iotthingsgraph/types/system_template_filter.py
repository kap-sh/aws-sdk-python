"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#SystemTemplateFilter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotthingsgraph.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.system_template_filter_name
    import aws_sdk_iotthingsgraph.types.system_template_filter_values


class SystemTemplateFilter(TypedDict):
    name: "aws_sdk_iotthingsgraph.types.system_template_filter_name.SystemTemplateFilterName"
    """<p>The name of the system search filter field.</p>"""
    value: "aws_sdk_iotthingsgraph.types.system_template_filter_values.SystemTemplateFilterValues"
    """<p>An array of string values for the search filter field. Multiple values function as AND criteria in the search.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SystemTemplateFilter) -> dict:
    out: dict = {}
    import aws_sdk_iotthingsgraph.types.system_template_filter_name

    out["name"] = (
        aws_sdk_iotthingsgraph.types.system_template_filter_name.serialize_aws_json_1_1(
            value["name"]
        )
    )
    import aws_sdk_iotthingsgraph.types.system_template_filter_values

    out["value"] = (
        aws_sdk_iotthingsgraph.types.system_template_filter_values.serialize_aws_json_1_1(
            value["value"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SystemTemplateFilter:
    out: SystemTemplateFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_iotthingsgraph.types.system_template_filter_name

        out["name"] = (
            aws_sdk_iotthingsgraph.types.system_template_filter_name.deserialize_aws_json_1_1(
                data["name"]
            )
        )
    else:
        raise DeserializationError("SystemTemplateFilter.name required")
    if "value" in data:
        import aws_sdk_iotthingsgraph.types.system_template_filter_values

        out["value"] = (
            aws_sdk_iotthingsgraph.types.system_template_filter_values.deserialize_aws_json_1_1(
                data["value"]
            )
        )
    else:
        raise DeserializationError("SystemTemplateFilter.value required")
    return out
