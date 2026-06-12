"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#SystemInstanceFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.system_instance_filter_name
    import aws_sdk_iotthingsgraph.types.system_instance_filter_values


class SystemInstanceFilter(TypedDict):
    name: NotRequired[
        "aws_sdk_iotthingsgraph.types.system_instance_filter_name.SystemInstanceFilterName"
    ]
    """<p>The name of the search filter field.</p>"""
    value: NotRequired[
        "aws_sdk_iotthingsgraph.types.system_instance_filter_values.SystemInstanceFilterValues"
    ]
    """<p>An array of string values for the search filter field. Multiple values function as AND criteria in the search. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SystemInstanceFilter) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_iotthingsgraph.types.system_instance_filter_name

        out["name"] = (
            aws_sdk_iotthingsgraph.types.system_instance_filter_name.serialize_aws_json_1_1(
                value["name"]
            )
        )
    if "value" in value:
        import aws_sdk_iotthingsgraph.types.system_instance_filter_values

        out["value"] = (
            aws_sdk_iotthingsgraph.types.system_instance_filter_values.serialize_aws_json_1_1(
                value["value"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SystemInstanceFilter:
    out: SystemInstanceFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_iotthingsgraph.types.system_instance_filter_name

        out["name"] = (
            aws_sdk_iotthingsgraph.types.system_instance_filter_name.deserialize_aws_json_1_1(
                data["name"]
            )
        )
    if "value" in data:
        import aws_sdk_iotthingsgraph.types.system_instance_filter_values

        out["value"] = (
            aws_sdk_iotthingsgraph.types.system_instance_filter_values.deserialize_aws_json_1_1(
                data["value"]
            )
        )
    return out
