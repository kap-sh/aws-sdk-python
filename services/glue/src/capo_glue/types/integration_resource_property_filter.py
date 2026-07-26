"""Generated from Smithy shape ``com.amazonaws.glue#IntegrationResourcePropertyFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.integration_resource_property_filter_values
    import capo_glue.types.string128


class IntegrationResourcePropertyFilter(TypedDict, closed=True):
    name: NotRequired["capo_glue.types.string128.String128"]
    """<p>The name of the filter. Supported filter keys are <code>SourceArn</code> and <code>TargetArn</code>.</p>"""
    values: NotRequired[
        "capo_glue.types.integration_resource_property_filter_values.IntegrationResourcePropertyFilterValues"
    ]
    """<p>A list of filter values.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IntegrationResourcePropertyFilter) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "values" in value:
        import capo_glue.types.integration_resource_property_filter_values

        out["Values"] = (
            capo_glue.types.integration_resource_property_filter_values.serialize_aws_json_1_1(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> IntegrationResourcePropertyFilter:
    out: IntegrationResourcePropertyFilter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Values" in data:
        import capo_glue.types.integration_resource_property_filter_values

        out["values"] = (
            capo_glue.types.integration_resource_property_filter_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    return out
