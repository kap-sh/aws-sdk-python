"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ExportFilter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_application_discovery_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.condition
    import aws_sdk_application_discovery_service.types.filter_name
    import aws_sdk_application_discovery_service.types.filter_values


class ExportFilter(TypedDict):
    name: "aws_sdk_application_discovery_service.types.filter_name.FilterName"
    """<p>A single <code>ExportFilter</code> name. Supported filters: <code>agentIds</code>.</p>"""
    values: "aws_sdk_application_discovery_service.types.filter_values.FilterValues"
    """<p>A single agent ID for a Discovery Agent. An agent ID can be found using the <a href=\"http://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeAgents.html\">DescribeAgents</a> action. Typically an ADS agent ID is in the form <code>o-0123456789abcdef0</code>.</p>"""
    condition: "aws_sdk_application_discovery_service.types.condition.Condition"
    """<p>Supported condition: <code>EQUALS</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportFilter) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> ExportFilter:
    out: ExportFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ExportFilter.name required")
    if "values" in data:
        import aws_sdk_application_discovery_service.types.filter_values

        out["values"] = (
            aws_sdk_application_discovery_service.types.filter_values.deserialize_aws_json_1_1(
                data["values"]
            )
        )
    else:
        raise DeserializationError("ExportFilter.values required")
    if "condition" in data:
        out["condition"] = data["condition"]
    else:
        raise DeserializationError("ExportFilter.condition required")
    return out
