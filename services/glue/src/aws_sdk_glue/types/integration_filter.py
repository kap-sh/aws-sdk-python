"""Generated from Smithy shape ``com.amazonaws.glue#IntegrationFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.integration_filter_values
    import aws_sdk_glue.types.string128


class IntegrationFilter(TypedDict, closed=True):
    name: NotRequired["aws_sdk_glue.types.string128.String128"]
    """<p>The name of the filter.</p>"""
    values: NotRequired[
        "aws_sdk_glue.types.integration_filter_values.IntegrationFilterValues"
    ]
    """<p>A list of filter values.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IntegrationFilter) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "values" in value:
        import aws_sdk_glue.types.integration_filter_values

        out["Values"] = (
            aws_sdk_glue.types.integration_filter_values.serialize_aws_json_1_1(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> IntegrationFilter:
    out: IntegrationFilter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Values" in data:
        import aws_sdk_glue.types.integration_filter_values

        out["values"] = (
            aws_sdk_glue.types.integration_filter_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    return out
