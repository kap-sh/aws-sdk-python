"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#Filter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_application_discovery_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.condition
    import aws_sdk_application_discovery_service.types.filter_values
    import aws_sdk_application_discovery_service.types.string


class Filter(TypedDict):
    name: "aws_sdk_application_discovery_service.types.string.String"
    """<p>The name of the filter.</p>"""
    values: "aws_sdk_application_discovery_service.types.filter_values.FilterValues"
    """<p>A string value on which to filter. For example, if you choose the <code>destinationServer.osVersion</code> filter name, you could specify <code>Ubuntu</code> for the value.</p>"""
    condition: "aws_sdk_application_discovery_service.types.condition.Condition"
    """<p>A conditional operator. The following operators are valid: EQUALS, NOT_EQUALS, CONTAINS, NOT_CONTAINS. If you specify multiple filters, the system utilizes all filters as though concatenated by <i>AND</i>. If you specify multiple values for a particular filter, the system differentiates the values using <i>OR</i>. Calling either <i>DescribeConfigurations</i> or <i>ListConfigurations</i> returns attributes of matching configuration items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Filter) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_application_discovery_service.types.filter_values

    out["values"] = (
        aws_sdk_application_discovery_service.types.filter_values.serialize_aws_json_1_1(
            value["values"]
        )
    )
    out["condition"] = value["condition"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Filter.name required")
    if "values" in data:
        import aws_sdk_application_discovery_service.types.filter_values

        out["values"] = (
            aws_sdk_application_discovery_service.types.filter_values.deserialize_aws_json_1_1(
                data["values"]
            )
        )
    else:
        raise DeserializationError("Filter.values required")
    if "condition" in data:
        out["condition"] = data["condition"]
    else:
        raise DeserializationError("Filter.condition required")
    return out
